import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class VisualCat:

    def visualcat(self, data, kolomx):
        df = data
        plt.figure(figsize=(5, 5))
        sns.countplot(df, x=kolomx)
        plt.xlabel(f"Data {kolomx}")
        plt.title(f"Visualisasi Variabel Category {kolomx}")
        plt.show()
