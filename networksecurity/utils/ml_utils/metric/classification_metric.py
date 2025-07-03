import sys

from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException

from sklearn.metrics import f1_score, recall_score, precision_score


def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:

    try:
        model_f1score = f1_score(y_true, y_pred)
        model_recall = recall_score(y_true, y_pred)
        model_precision_score = precision_score(y_true, y_pred)

        classification_metric_artifiact = ClassificationMetricArtifact(
            f1_score=model_f1score,
            recall_score=model_recall,
            precision_score=model_precision_score
        )
        return classification_metric_artifiact
    except Exception as e:
        raise NetworkSecurityException(e, sys)