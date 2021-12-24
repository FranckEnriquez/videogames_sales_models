# import external libraries
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def time_series_plot(df, x_col, y_col, title):
    '''
    Plot of a time series univariate or multivariate
    '''
    if y_col == True:
        # Multivariate series
        fig = px.line(df, x=x_col, y=df.columns, title=title)
    else:
        # Univariate series
        fig = px.line(df, x=x_col, y=y_col, title=title)
    return fig.show()


def histogram_plot(df, rand_var, nbins, title):
    '''
    Plot a histogram distribution according its frequencies
    '''
    fig = px.histogram(df, x=rand_var, nbins=nbins, title=title)
    return fig.show()


def box_plot(df, rand_var, title):
    '''
    Boxplot of a variable
    '''
    fig = px.box(df, y=rand_var, orientation='v', title=title)
    return fig.show()


def bar_plot(df, x_col, y_col, title):
    '''
    Bar plot of a variable
    '''
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    return fig.show()


def heatmap_corr(df):
    '''
    A heatmap plot shows correlations
    '''

    # set the limits
    heatmap = sns.heatmap(df.corr(), cmap="YlGnBu",
                          vmin=0, vmax=1, annot=True)

    ht = heatmap.set_title('Mapa de calor de correlaciones',
                           fontdict={'fontsize': 12}, pad=12)

    return ht
