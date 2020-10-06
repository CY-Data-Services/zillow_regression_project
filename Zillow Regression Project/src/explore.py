import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
from scipy import stats

import warnings
warnings.filterwarnings("ignore")

###################### Explore ######################

def plot_variable_pairs(df):
    '''
    Function that plots all of the pairwise relationships along with the regression line for each pair
    '''
    g = sns.PairGrid(df)    
    g.map_diag(sns.distplot)  
    g.map_offdiag(sns.regplot)
    plt.show()
    return g


def plot_categorical_and_continuous_vars(df, categorical_var, continuous_var):
    '''
    Function that outputs 3 different plots for plotting a categorical variable with a continuous variable
    '''
    sns.barplot(data=df, y=continuous_var, x=categorical_var)
    plt.show()
    sns.violinplot(data=df, y=continuous_var, x=categorical_var)
    plt.show()
    sns.boxplot(data=df, y=continuous_var, x=categorical_var)

def run():
    print("Model: Running models...")
    # Write code here
    print("Model: Completed!")

def run():
    print("Explore: Generating visuals...")
    # Write code here
    print("Explore: Completed!")
