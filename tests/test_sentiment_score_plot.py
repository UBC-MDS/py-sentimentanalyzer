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
    """Assert function first input is dataframe"""
    df = pd.read_csv("test_tweets.csv")
    assert isinstance(df, pd.DataFrame), "first input should be type dataframe"


def test_function_input_column():
    """Assert function second input is a string"""
    df = pd.read_csv("test_tweets.csv")
    col = "text"
    assert isinstance(col, str), "column name should be string dtype"
