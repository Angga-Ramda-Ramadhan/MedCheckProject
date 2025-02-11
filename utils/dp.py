import pandas


class CheckDP:
    

    def checkdp(self, data):
        df = data.duplicated().sum()
        if df > 0:
            df = data.drop_duplicates()
            print("Data Duplikat berhasil di hapus")
            return df
        else:
            print("Tidak Ada Duplikat Data")
            return data