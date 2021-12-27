# import external libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


def cramers_v(x, y):
    '''
    Cramer's V helps to find the "correlation" between
    categorical varibles
    '''
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1), (rcorr-1)))


def preprocess(df, drop_cols):
    def label_feature(df):
        '''
        Selection of a label feature
        '''
        df['y'] = df['Global_Sales']
        df = df.drop(['Global_Sales'], axis = 1)
        return df

    df = label_feature(df)

    def drop_columns(df, drop_cols):
        '''
        Eliminates all the not necessary or duplicate
        columns
        '''
        df = df.drop(drop_cols, axis=1)
        return df

    df = drop_columns(df, drop_cols)
    return df
