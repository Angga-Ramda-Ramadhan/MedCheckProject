import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import VisualCat

class Exploratory:

    def __init__(self):
        self.visual = VisualCat()

    def visualisasi(self, data, kolomx):
        explor = self.visual.visualcat(data, kolomx)
        return explor