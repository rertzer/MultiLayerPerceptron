import random
import pandas as pd
from .config import *
from . import getdata as gd


class SplitData:
    def __init__(self, file_name: str):
        self.data = gd.get_data_csv(file_name)
        print(self.data)

    def split(self, data_ratio: float):
        if not self.checkValidRatio(data_ratio):
            return
        data_len = len(self.data)
        train_len = int(data_len * data_ratio)
        test_len = data_len - train_len
        print("data len:", data_len)
        print("train len:", train_len)
        print("test len:", test_len)

        random_indices = list(range(data_len))
        random.shuffle(random_indices)
        self.train_data = []
        self.test_data = []
        for i in range(train_len):
            index = random_indices[i]
            self.train_data.append(self.data.iloc[index])
        for i in range(train_len, data_len):
            index = random_indices[i]
            self.test_data.append(self.data.iloc[index])

        self.dataFrameFormat()
        self.dataFrameFormat()
        assert isinstance(self.test_data, pd.DataFrame)
        assert isinstance(self.train_data, pd.DataFrame)

        print("train len:", len(self.train_data))
        print("test len:", len(self.test_data))
        gd.save_data_csv(self.train_data, CSV_DIR + TRAIN_FILE)
        gd.save_data_csv(self.test_data, CSV_DIR + TEST_FILE)
        print(self.test_data)

    def checkValidRatio(self, value: float) -> bool:

        if not gd.is_valid_float(value) or value <= 0 or value > 1:
            print("Error: Data ratio should be between 0 and 1")
            return False
        return True

    def dataFrameFormat(self):
        cols = [
            "Index",
            "Diagnosis",
            "Radius mean",
            "Texture mean",
            "Perimeter mean",
            "Area mean",
            "Smoothness mean",
            "Compactness mean",
            "Concavity mean",
            "Concave Points mean",
            "Symmetry mean",
            "Fractal Dimension mean",
            "Radius SE",
            "Texture SE",
            "Perimeter SE",
            "Area SE",
            "Smoothness SE",
            "Compactness SE",
            "Concavity SE",
            "Concave Points SE",
            "Symmetry SE",
            "Fractal Dimension SE",
            "Radius Worst",
            "Texture Worst",
            "Perimeter Worst",
            "Area Worst",
            "Smoothness Worst",
            "Compactness Worst",
            "Concavity Worst",
            "Concave Points Worst",
            "Symmetry Worst",
            "Fractal Dimension Worst",
        ]

        self.train_data = pd.DataFrame(self.train_data)
        self.test_data = pd.DataFrame(self.test_data)
        self.train_data.columns = cols
        self.test_data.columns = cols


if __name__ == "__main__":
    sd = SplitData(CSV_DIR + DATA_FILE)
    sd.split(0.8)
