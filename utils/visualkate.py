import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class VisualCat:

    def visualcat(self, data, kolomx):
        df = data
        plt.figure(figsize=(5, 5))
        sns.countplot(df, x=kolomx, hue=kolomx)
        plt.xlabel(f"Data {kolomx}")
        plt.title(f"Visualisasi Variabel Category {kolomx}")
        plt.show()
    
    def func_visual_catplot(self, data, kolomx):
        plt.figure(figsize=(6,6))
        sns.catplot(data, x= kolomx)
        plt.xlabel(f"Data {kolomx}")
        plt.title(f'Visualisasi Catplot Data {kolomx}')
        plt.show()
    
    def func_visual_catplot_double(self, data, kolomx, kolomy):
        plt.figure(figsize=(6,6))
        sns.catplot(data, x= kolomx, y=kolomy, hue=kolomx)
        plt.xlabel(f"Data {kolomx}")
        plt.title(f'Visualisasi Bivariate Catplot Data {kolomx} dan {kolomy}')
        plt.show()
