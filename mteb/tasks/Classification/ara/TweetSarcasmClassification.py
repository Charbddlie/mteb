from __future__ import annotations

from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class TweetSarcasmClassification(AbsTaskClassification):
    superseded_by = "TweetSarcasmClassification.v2"
    metadata = TaskMetadata(
        name="TweetSarcasmClassification",
        dataset={
            "path": "iabufarha/ar_sarcasm",
            "revision": "557bf94ac6177cc442f42d0b09b6e4b76e8f47c9",
        },
        description="Arabic sarcasm detection dataset, which was created through the reannotation of available Arabic sentiment analysis datasets.",
        reference="https://aclanthology.org/2020.osact-1.5/",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["ara-Arab"],
        main_score="accuracy",
        date=("2020-01-01", "2021-01-01"),
        domains=["Social", "Written"],
        task_subtypes=["Sentiment/Hate speech"],
        license="mit",
        annotations_creators="human-annotated",
        dialect=["ara-arab-EG", "ara-arab-LB", "ara-arab-MA", "ara-arab-SA"],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{abu-farha-magdy-2020-arabic,
  abstract = {Sarcasm is one of the main challenges for sentiment analysis systems. Its complexity comes from the expression of opinion using implicit indirect phrasing. In this paper, we present ArSarcasm, an Arabic sarcasm detection dataset, which was created through the reannotation of available Arabic sentiment analysis datasets. The dataset contains 10,547 tweets, 16{\%} of which are sarcastic. In addition to sarcasm the data was annotated for sentiment and dialects. Our analysis shows the highly subjective nature of these tasks, which is demonstrated by the shift in sentiment labels based on annotators{'} biases. Experiments show the degradation of state-of-the-art sentiment analysers when faced with sarcastic content. Finally, we train a deep learning model for sarcasm detection using BiLSTM. The model achieves an F1 score of 0.46, which shows the challenging nature of the task, and should act as a basic baseline for future research on our dataset.},
  address = {Marseille, France},
  author = {Abu Farha, Ibrahim  and
Magdy, Walid},
  booktitle = {Proceedings of the 4th Workshop on Open-Source Arabic Corpora and Processing Tools, with a Shared Task on Offensive Language Detection},
  editor = {Al-Khalifa, Hend  and
Magdy, Walid  and
Darwish, Kareem  and
Elsayed, Tamer  and
Mubarak, Hamdy},
  isbn = {979-10-95546-51-1},
  language = {English},
  month = may,
  pages = {32--39},
  publisher = {European Language Resource Association},
  title = {From {A}rabic Sentiment Analysis to Sarcasm Detection: The {A}r{S}arcasm Dataset},
  url = {https://aclanthology.org/2020.osact-1.5},
  year = {2020},
}
""",
    )

    def dataset_transform(self):
        # labels: 0 non-sarcastic, 1 sarcastic
        self.dataset = self.dataset.rename_columns(
            {"tweet": "text", "sarcasm": "label"}
        )


class TweetSarcasmClassificationV2(AbsTaskClassification):
    metadata = TaskMetadata(
        name="TweetSarcasmClassification.v2",
        dataset={
            "path": "mteb/tweet_sarcasm",
            "revision": "3a20898e2ea3303844e907d55f7a815a7644150d",
        },
        description="""Arabic sarcasm detection dataset, which was created through the reannotation of available Arabic sentiment analysis datasets.
        This version corrects errors found in the original data. For details, see [pull request](https://github.com/embeddings-benchmark/mteb/pull/2632)""",
        reference="https://aclanthology.org/2020.osact-1.5/",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["ara-Arab"],
        main_score="accuracy",
        date=("2020-01-01", "2021-01-01"),
        domains=["Social", "Written"],
        task_subtypes=["Sentiment/Hate speech"],
        license="mit",
        annotations_creators="human-annotated",
        dialect=["ara-arab-EG", "ara-arab-LB", "ara-arab-MA", "ara-arab-SA"],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{abu-farha-magdy-2020-arabic,
  abstract = {Sarcasm is one of the main challenges for sentiment analysis systems. Its complexity comes from the expression of opinion using implicit indirect phrasing. In this paper, we present ArSarcasm, an Arabic sarcasm detection dataset, which was created through the reannotation of available Arabic sentiment analysis datasets. The dataset contains 10,547 tweets, 16{\%} of which are sarcastic. In addition to sarcasm the data was annotated for sentiment and dialects. Our analysis shows the highly subjective nature of these tasks, which is demonstrated by the shift in sentiment labels based on annotators{'} biases. Experiments show the degradation of state-of-the-art sentiment analysers when faced with sarcastic content. Finally, we train a deep learning model for sarcasm detection using BiLSTM. The model achieves an F1 score of 0.46, which shows the challenging nature of the task, and should act as a basic baseline for future research on our dataset.},
  address = {Marseille, France},
  author = {Abu Farha, Ibrahim  and
Magdy, Walid},
  booktitle = {Proceedings of the 4th Workshop on Open-Source Arabic Corpora and Processing Tools, with a Shared Task on Offensive Language Detection},
  editor = {Al-Khalifa, Hend  and
Magdy, Walid  and
Darwish, Kareem  and
Elsayed, Tamer  and
Mubarak, Hamdy},
  isbn = {979-10-95546-51-1},
  language = {English},
  month = may,
  pages = {32--39},
  publisher = {European Language Resource Association},
  title = {From {A}rabic Sentiment Analysis to Sarcasm Detection: The {A}r{S}arcasm Dataset},
  url = {https://aclanthology.org/2020.osact-1.5},
  year = {2020},
}
""",
    )
