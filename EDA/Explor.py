import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import VisualCat

class Exploratory:

    def __init__(self):
        self.visual = VisualCat()

    def visualcount(self, data, kolomx):
        explor = self.visual.visualcat(data, kolomx)
        return explor
    
    def visualcatplot(self, data, kolomx):
        explor = self.visual.func_visual_catplot(data, kolomx)
        return explor
    
    def visualcatplotdouble(self, data, kolomx, kolomy):
        explor = self.visual.func_visual_catplot_double(data, kolomx, kolomy)
        return explor