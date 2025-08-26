from src.data_loader import CWRUDataLoader
from src.logger import logging

if __name__ == "__main__":
    logging.info("Starting pipeline...")

    loader = CWRUDataLoader()
    try:
        signal = loader.load_raw("B007_1_123.mat")  
        df = loader.preprocess(signal, label="healthy")
        path = loader.save_preprocessed(df)
        logging.info(f"Pipeline step completed, data saved at {path}")
    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")

    logging.info("Pipeline finished.")
