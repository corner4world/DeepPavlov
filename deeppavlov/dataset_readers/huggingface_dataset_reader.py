# Copyright 2020 Neural Networks and Deep Learning lab, MIPT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import re
from typing import Dict, Optional, List

from datasets import load_dataset, Dataset
from overrides import overrides

from deeppavlov.core.common.registry import register
from deeppavlov.core.data.dataset_reader import DatasetReader


@register('huggingface_dataset_reader')
class HuggingFaceDatasetReader(DatasetReader):
    """Adds HuggingFace Datasets https://huggingface.co/datasets/ to DeepPavlov
    """

    @overrides
    def read(self,
             data_path: str,
             path: str,
             name: Optional[str] = None,
             train: str = 'train',
             valid: Optional[str] = None,
             test: Optional[str] = None,
             **kwargs) -> Dict[str, Dataset]:
        """Wraps datasets.load_dataset method

        Args:
            data_path: DeepPavlov's data_path argument, is not used, but passed by trainer
            path: datasets.load_dataset path argument (e.g., `glue`)
            name: datasets.load_dataset name argument (e.g., `mrpc`)
            train: split name to use as training data.
            valid: split name to use as validation data.
            test: split name to use as test data.

        Returns:
            Dict[str, List[Dict]]: Dictionary with train, valid, test datasets
        """
        if 'split' in kwargs:
            raise RuntimeError('Split argument was used. Use train, valid, test arguments instead of split.')
        split_mapping = {'train': train, 'valid': valid, 'test': test}
        # filter unused splits
        split_mapping = {el: split_mapping[el] for el in split_mapping if split_mapping[el]}
        dataset = load_dataset(path=path, name=name, split=list(split_mapping.values()), **kwargs)
        if path == "super_glue" and name == "copa":
            dataset = [dataset_split.map(preprocess_copa, batched=True) for dataset_split in dataset]
        elif path == "super_glue" and name == "boolq":
            dataset = load_dataset(path=path, name=name, split=interleave_splits(list(split_mapping.values())), **kwargs)
            dataset = [dataset_split.map(preprocess_boolq, batched=True) for dataset_split in dataset]
        return dict(zip(split_mapping.keys(), dataset))


def interleave_splits(splits: List[str]) -> List[str]:
    return [f"{splits[0]}+{splits[1]}[:50%]", f"{splits[1]}[-50%:]", splits[2]]


def preprocess_copa(examples: Dataset) -> Dict[str, List[List[str]]]:
    question_dict = {
        "cause": "What was the cause of this?",
        "effect": "What happened as a result?",
    }

    num_choices = 2

    questions = [question_dict[question] for question in examples["question"]]
    premises = examples["premise"]

    contexts = [f"{premise} {question}" for premise, question in zip(premises, questions)]
    contexts = [[context] * num_choices for context in contexts]

    choices = [[choice1, choice2] for choice1, choice2 in zip(examples["choice1"], examples["choice2"])]

    return {"contexts": contexts,
            "choices": choices}


def preprocess_boolq(examples: Dataset) -> Dict[str, List[str]]:

    def remove_passage_title(passage: str) -> str:
        return re.sub(r"^.+-- ", "", passage)

    passages = [remove_passage_title(passage) for passage in examples["passage"]]

    return {"passage": passages}
