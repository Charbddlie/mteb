from __future__ import annotations

from itertools import chain

import numpy as np
from datasets import Dataset, DatasetDict

from mteb.abstasks.AbsTaskClustering import AbsTaskClustering
from mteb.abstasks.AbsTaskClusteringFast import (
    AbsTaskClusteringFast,
    check_label_distribution,
)
from mteb.abstasks.TaskMetadata import TaskMetadata

N_SAMPLES = 2048


class EightTagsClustering(AbsTaskClustering):
    superseded_by = "EightTagsClustering.v2"
    metadata = TaskMetadata(
        name="EightTagsClustering",
        description="Clustering of headlines from social media posts in Polish belonging to 8 categories: film, history, "
        + "food, medicine, motorization, work, sport and technology.",
        reference="https://aclanthology.org/2020.lrec-1.207.pdf",
        dataset={
            "path": "PL-MTEB/8tags-clustering",
            "revision": "78b962b130c6690659c65abf67bf1c2f030606b6",
        },
        type="Clustering",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["pol-Latn"],
        main_score="v_measure",
        date=("2019-01-01", "2020-05-01"),
        domains=["Social", "Written"],
        task_subtypes=["Topic classification", "Thematic clustering"],
        license="gpl-3.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{dadas-etal-2020-evaluation,
  abstract = {Methods for learning sentence representations have been actively developed in recent years. However, the lack of pre-trained models and datasets annotated at the sentence level has been a problem for low-resource languages such as Polish which led to less interest in applying these methods to language-specific tasks. In this study, we introduce two new Polish datasets for evaluating sentence embeddings and provide a comprehensive evaluation of eight sentence representation methods including Polish and multilingual models. We consider classic word embedding models, recently developed contextual embeddings and multilingual sentence encoders, showing strengths and weaknesses of specific approaches. We also examine different methods of aggregating word vectors into a single sentence vector.},
  address = {Marseille, France},
  author = {Dadas, Slawomir  and
Pere{\\l}kiewicz, Micha{\\l}  and
Po{\\'s}wiata, Rafa{\\l}},
  booktitle = {Proceedings of the Twelfth Language Resources and Evaluation Conference},
  editor = {Calzolari, Nicoletta  and
B{\'e}chet, Fr{\'e}d{\'e}ric  and
Blache, Philippe  and
Choukri, Khalid  and
Cieri, Christopher  and
Declerck, Thierry  and
Goggi, Sara  and
Isahara, Hitoshi  and
Maegaard, Bente  and
Mariani, Joseph  and
Mazo, H{\\'e}l{\\`e}ne  and
Moreno, Asuncion  and
Odijk, Jan  and
Piperidis, Stelios},
  isbn = {979-10-95546-34-4},
  language = {English},
  month = may,
  pages = {1674--1680},
  publisher = {European Language Resources Association},
  title = {Evaluation of Sentence Representations in {P}olish},
  url = {https://aclanthology.org/2020.lrec-1.207},
  year = {2020},
}
""",
    )


class EightTagsClusteringFast(AbsTaskClusteringFast):
    max_document_to_embed = N_SAMPLES
    max_fraction_of_documents_to_embed = None

    metadata = TaskMetadata(
        name="EightTagsClustering.v2",
        description="Clustering of headlines from social media posts in Polish belonging to 8 categories: film, history, "
        + "food, medicine, motorization, work, sport and technology.",
        reference="https://aclanthology.org/2020.lrec-1.207.pdf",
        dataset={
            "path": "PL-MTEB/8tags-clustering",
            "revision": "78b962b130c6690659c65abf67bf1c2f030606b6",
        },
        type="Clustering",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["pol-Latn"],
        main_score="v_measure",
        date=("2019-01-01", "2020-05-01"),
        domains=["Social", "Written"],
        task_subtypes=["Topic classification", "Thematic clustering"],
        license="gpl-3.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{dadas-etal-2020-evaluation,
  abstract = {Methods for learning sentence representations have been actively developed in recent years. However, the lack of pre-trained models and datasets annotated at the sentence level has been a problem for low-resource languages such as Polish which led to less interest in applying these methods to language-specific tasks. In this study, we introduce two new Polish datasets for evaluating sentence embeddings and provide a comprehensive evaluation of eight sentence representation methods including Polish and multilingual models. We consider classic word embedding models, recently developed contextual embeddings and multilingual sentence encoders, showing strengths and weaknesses of specific approaches. We also examine different methods of aggregating word vectors into a single sentence vector.},
  address = {Marseille, France},
  author = {Dadas, Slawomir  and
Pere{\\l}kiewicz, Micha{\\l}  and
Po{\\'s}wiata, Rafa{\\l}},
  booktitle = {Proceedings of the Twelfth Language Resources and Evaluation Conference},
  editor = {Calzolari, Nicoletta  and
B{\\'e}chet, Fr{\\'e}d{\\'e}ric  and
Blache, Philippe  and
Choukri, Khalid  and
Cieri, Christopher  and
Declerck, Thierry  and
Goggi, Sara  and
Isahara, Hitoshi  and
Maegaard, Bente  and
Mariani, Joseph  and
Mazo, H{\\'e}l{\\`e}ne  and
Moreno, Asuncion  and
Odijk, Jan  and
Piperidis, Stelios},
  isbn = {979-10-95546-34-4},
  language = {English},
  month = may,
  pages = {1674--1680},
  publisher = {European Language Resources Association},
  title = {Evaluation of Sentence Representations in {P}olish},
  url = {https://aclanthology.org/2020.lrec-1.207},
  year = {2020},
}
""",
        adapted_from=["EightTagsClustering"],
    )

    def dataset_transform(self):
        ds = {}
        for split in self.metadata.eval_splits:
            labels = list(chain.from_iterable(self.dataset[split]["labels"]))
            sentences = list(chain.from_iterable(self.dataset[split]["sentences"]))
            check_label_distribution(self.dataset[split])

            ds[split] = Dataset.from_dict({"labels": labels, "sentences": sentences})
        self.dataset = DatasetDict(ds)
        self.dataset = self.stratified_subsampling(
            self.dataset,
            self.seed,
            self.metadata.eval_splits,
            label="labels",
            n_samples=N_SAMPLES,
        )


class PlscClusteringS2S(AbsTaskClusteringFast):
    superseded_by = "PlscClusteringS2S.v2"
    metadata = TaskMetadata(
        name="PlscClusteringS2S",
        description="Clustering of Polish article titles from Library of Science (https://bibliotekanauki.pl/), either "
        + "on the scientific field or discipline.",
        reference="https://huggingface.co/datasets/rafalposwiata/plsc",
        dataset={
            "path": "PL-MTEB/plsc-clustering-s2s",
            "revision": "39bcadbac6b1eddad7c1a0a176119ce58060289a",
        },
        type="Clustering",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["pol-Latn"],
        main_score="v_measure",
        date=("2022-04-04", "2023-09-12"),
        domains=["Academic", "Written"],
        task_subtypes=["Topic classification", "Thematic clustering"],
        license="cc0-1.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="",
    )


class PlscClusteringS2SFast(AbsTaskClusteringFast):
    metadata = TaskMetadata(
        name="PlscClusteringS2S.v2",
        description="Clustering of Polish article titles from Library of Science (https://bibliotekanauki.pl/), either "
        + "on the scientific field or discipline.",
        reference="https://huggingface.co/datasets/rafalposwiata/plsc",
        dataset={
            "path": "PL-MTEB/plsc-clustering-s2s",
            "revision": "39bcadbac6b1eddad7c1a0a176119ce58060289a",
        },
        type="Clustering",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["pol-Latn"],
        main_score="v_measure",
        date=("2022-04-04", "2023-09-12"),
        domains=["Academic", "Written"],
        task_subtypes=["Topic classification", "Thematic clustering"],
        license="cc0-1.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="",
        adapted_from=["PlscClusteringS2S"],
    )

    def dataset_transform(self):
        ds = {}
        for split in self.metadata.eval_splits:
            labels = self.dataset[split]["labels"]
            sentences = self.dataset[split]["sentences"]

            check_label_distribution(self.dataset[split])

            # Remove sentences and labels with only 1 label example.
            unique_labels, counts = np.unique(labels, return_counts=True)
            solo_label_idx = np.where(counts == 1)
            solo_labels = unique_labels[solo_label_idx]
            is_solo = np.isin(labels, solo_labels)
            split_ds = Dataset.from_dict({"labels": labels, "sentences": sentences})
            if is_solo.any():
                split_ds = split_ds.select(np.nonzero(is_solo == False)[0])  # noqa: E712
            ds[split] = split_ds
        self.dataset = DatasetDict(ds)
        self.dataset = self.stratified_subsampling(
            self.dataset,
            self.seed,
            self.metadata.eval_splits,
            label="labels",
            n_samples=N_SAMPLES,
        )


class PlscClusteringP2P(AbsTaskClusteringFast):
    superseded_by = "PlscClusteringP2P.v2"
    metadata = TaskMetadata(
        name="PlscClusteringP2P",
        description="Clustering of Polish article titles+abstracts from Library of Science "
        + "(https://bibliotekanauki.pl/), either on the scientific field or discipline.",
        reference="https://huggingface.co/datasets/rafalposwiata/plsc",
        dataset={
            "path": "PL-MTEB/plsc-clustering-p2p",
            "revision": "8436dd4c05222778013d6642ee2f3fa1722bca9b",
        },
        type="Clustering",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["pol-Latn"],
        main_score="v_measure",
        date=("2022-04-04", "2023-09-12"),
        domains=["Academic", "Written"],
        task_subtypes=["Topic classification", "Thematic clustering"],
        license="cc0-1.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="",
    )


class PlscClusteringP2PFast(AbsTaskClusteringFast):
    metadata = TaskMetadata(
        name="PlscClusteringP2P.v2",
        description="Clustering of Polish article titles+abstracts from Library of Science "
        + "(https://bibliotekanauki.pl/), either on the scientific field or discipline.",
        reference="https://huggingface.co/datasets/rafalposwiata/plsc",
        dataset={
            "path": "PL-MTEB/plsc-clustering-p2p",
            "revision": "8436dd4c05222778013d6642ee2f3fa1722bca9b",
        },
        type="Clustering",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["pol-Latn"],
        main_score="v_measure",
        date=("2022-04-04", "2023-09-12"),
        domains=["Academic", "Written"],
        task_subtypes=["Topic classification", "Thematic clustering"],
        license="cc0-1.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="",
        adapted_from=["PlscClusteringP2P"],
    )

    def dataset_transform(self):
        ds = {}
        for split in self.metadata.eval_splits:
            labels = self.dataset[split]["labels"]
            sentences = self.dataset[split]["sentences"]

            check_label_distribution(self.dataset[split])

            # Remove sentences and labels with only 1 label example.
            unique_labels, counts = np.unique(labels, return_counts=True)
            solo_label_idx = np.where(counts == 1)
            solo_labels = unique_labels[solo_label_idx]
            is_solo = np.isin(labels, solo_labels)
            split_ds = Dataset.from_dict({"labels": labels, "sentences": sentences})
            if is_solo.any():
                split_ds = split_ds.select(np.nonzero(is_solo == False)[0])  # noqa: E712
            ds[split] = split_ds
        self.dataset = DatasetDict(ds)
        self.dataset = self.stratified_subsampling(
            self.dataset,
            self.seed,
            self.metadata.eval_splits,
            label="labels",
            n_samples=N_SAMPLES,
        )
