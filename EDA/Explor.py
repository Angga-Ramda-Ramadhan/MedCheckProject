import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import VisualCat

class Exploratory:

    def __init__(self):
        self.visual = VisualCat()

    def visualcount(self, data, jk, jb):
        explor = self.visual.visualcat(data, jk, jb)
        return explor
    
    def visualcatplot(self, data, jk, jb):
        explor = self.visual.func_visual_catplot(data, jk, jb)
        return explor
    
    def visualcatplotdouble(self, data, jk, jb, target):
        explor = self.visual.func_visual_countplot_double(data, jk, jb, target)
        return explor
    
    
    def visualnumvar(self, data_num, jk, jb):
        explor = self.visual.func_visual_num_dist(data_num, jk, jb)
        return explor