import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    vector = np.asarray(x, dtype=float)
    return 1/(1+np.exp(-vector))