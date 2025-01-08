import pandas as pd
from utils import CheckDP, CheckMV
import seaborn as sns

class Preprocessor:
    
    def __init__(self):
        self.cdp = CheckDP()
        self.cmv = CheckMV()

    def cleaning_mv_and_dp(self, data):
        df = self.cdp.checkdp(data)
        df_clean = self.cmv.checkmv(df)
        return df_clean
    
    def clean_outlier(self, data, kolom):
        Q1 = data[kolom].quantile(0.25)
        Q3 = data[kolom].quantile(0.75)
        IQR = Q3 - Q1
        upper_bond = Q3 + 1.5 * IQR
        lower_bond = Q1 - 1.5 * IQR

        data_clean = data[(data[kolom] <= upper_bond) | (data[kolom] >= lower_bond)]
        sns.boxplot(data_clean, y= kolom)

        return data_clean
