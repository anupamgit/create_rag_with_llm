import pandas as pd


class DataLoader:
    def __init__(self, file_name, na_fields, sample_size=0):
        self.file = file_name
        self.df = pd.read_csv(file_name)
        for field in na_fields:
            self.df = self.df[self.df[field].notna()]
        if sample_size == 0:
            self.data = self.df.to_dict("records")
        else:
            self.data = self.df.sample(sample_size).to_dict("records")

    def get_data(self):
        return self.data
