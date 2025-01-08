import pandas


class CheckDP:
    

    def checkdp(self, data):
        df = data.duplicated().sum()
        if df > 0:
            df = data.drop_duplicates()
            print("Data berhasil di hapus")
            return df
        else:
            print("Data bersih")
            return data