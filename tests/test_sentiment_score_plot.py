import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pysentimentanalyzer import sentiment_score_plot


def test_function_returns_figure():
    """Assert function returns a matplotlob object"""
    df = pd.read_csv("test_tweets.csv")
    col = "text"
    plot = sentiment_score_plot.sentiment_score_plot(df, col)
    assert isinstance(
        plot, matplotlib.figure.Figure
    ), "returned object is not a plot object"


def test_function_input_dataframe():
    """Assert not passing first input as dataframe to function"""
    with pytest.raises(TypeError):
        sentiment_score_plot("not a dataframe", "column")


def test_function_input_column():
    """Assert not passing second input as a string to function"""
    df = pd.read_csv("test_tweets.csv")
    with pytest.raises(TypeError):
        sentiment_score_plot(df, 45)


def test_function_column_missing():
    """Assert passed column to function does not exist"""
    df = pd.read_csv("test_tweets.csv")
    with pytest.raises(Exception):
        sentiment_score_plot(df, "non existent column")
