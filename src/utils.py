import numpy as np

def normalize_signal(signal):
    """Normalize signal between -1 and 1"""
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal)) * 2 - 1
