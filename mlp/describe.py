import pandas as pd

from .config import *


from .feature import Feature


class Describe:
    def __init__(self, file_name):

        datas = pd.read_csv(file_name)
        self.num_data = datas.select_dtypes(include=[float, int])
        self.num_data.drop(columns=[INDEX_COLUMN], inplace=True)

    def describe(self):
        self.analyzed: dict[str, list] = {}

        for col in self.num_data.columns:
            feature = Feature(self.num_data[col])  # type: ignore[arg-type]
            feature.analyse()
            self.analyzed[col] = feature.getStats()

    def print(self):

        df = pd.DataFrame(
            self.analyzed,
            index=[
                "count",
                "mean",
                "std",
                "min",
                "25%",
                "50%",
                "75%",
                "max",
                "kurtosis",
                "skewness",
            ],
        )
        print(df.iloc[:, 0:10], "\n")
        print(df.iloc[:, 10:20], "\n")
        print(df.iloc[:, 20:30])


if __name__ == "__main__":
    desc = Describe(CSV_DIR + TRAIN_FILE)
    desc.describe()
    desc.print()

    # print(desc.num_data.describe())
    # print(desc.num_data.kurtosis())
    # print(desc.num_data.skew())
