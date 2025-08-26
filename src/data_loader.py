import os
import pandas as pd
from src.logger import logging
import scipy

class CWRUDataLoader:
    def __init__(self, raw_dir="data/cwru/raw", processed_dir="data/cwru/processed"):
        self.raw_dir = raw_dir
        self.processed_dir = processed_dir
        os.makedirs(self.processed_dir, exist_ok=True)

    def load_raw(self, filename):
        """Load raw MAT vibration file"""
        file_path = os.path.join(self.raw_dir, filename)
        logging.info(f"Loading raw file: {file_path}")
        mat_data = scipy.io.loadmat(file_path)
        key = [k for k in mat_data.keys() if "DE_time" in k][0]
        signal = mat_data[key].squeeze()
        return signal

    def preprocess(self, signal, label, window_size=1024):
        """Convert signal into overlapping windows with labels"""
        samples = []
        for i in range(0, len(signal) - window_size, window_size):
            segment = signal[i:i+window_size]
            samples.append((segment.tolist(), label))
        df = pd.DataFrame(samples, columns=["signal", "label"])
        return df

    def save_preprocessed(self, df, name="cwru_processed.csv"):
        path = os.path.join(self.processed_dir, name)
        df.to_csv(path, index=False)
        logging.info(f"Saved preprocessed data to {path}")
        return path
