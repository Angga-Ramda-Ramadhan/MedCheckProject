import pandas as pd


class CheckMV:

    def checkmv(self, data):
        df = data.isnull().sum().sum()
        if df > 0:
            df = df.dropna()
            print("Berhasil Hapus MV")
            return df
        else:
            print("tidak ada MV")
            return data