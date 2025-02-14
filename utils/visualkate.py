import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class VisualCat:


    def visualcat(self, data, jumlah_kolom, jumlah_baris):
        plt.figure(figsize=(12, 6))
        for i, col in enumerate(data.columns, 1):
            plt.subplot(jumlah_baris, jumlah_kolom, i)
            sns.countplot(data, x=col, hue=col)
            plt.xlabel(f"Data {col}")
            plt.title(f"Visualisasi Variabel Category {col}")
        plt.tight_layout()
        plt.show()
    

    def func_visual_catplot(self, data, jumlah_kolom, jumlah_baris):
        plt.figure(figsize=(12,6))
        for i, col in enumerate(data.columns, 1):
            plt.subplot(jumlah_baris, jumlah_kolom, i)
            sns.boxplot(data, y=col)
            plt.xlabel(f"Data {col}")
            plt.title(f'Visualisasi Catplot Data {col}')     
        plt.tight_layout()
        plt.show()


    def func_visual_countplot_double(self, data, jumlah_kolom, jumlah_baris, target):
        plt.figure(figsize=(12,8))
        for i, col in enumerate(data.columns, 1):
            plt.subplot(jumlah_baris, jumlah_kolom, i)
            sns.countplot(data, x= col, hue=target)
            plt.xlabel(f"Data {col}")
            plt.title(f'Visualisasi Bivariate Countplot Data {col}')
        plt.tight_layout()
        plt.show()


    def func_visual_num_dist(self, data_num, jumlah_kolom, jumlah_row):
        plt.figure(figsize=(12,4))
        for i, col in enumerate(data_num.columns, 1):
            plt.subplot(jumlah_row, jumlah_kolom, i)
            sns.histplot(data_num, x=col, kde=True)
            plt.title(f'Visualisasi Univariate Numerical Var {col}')
            plt.xlabel(f'Kolom {col}')
        plt.tight_layout()
        plt.show()