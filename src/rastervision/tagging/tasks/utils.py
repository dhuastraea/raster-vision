import numpy as np


def compute_prediction(y_probs, dataset, tag_store, thresholds=None):
    y_pred = (y_probs > thresholds).astype(np.float32)

    # TODO

    return y_pred
