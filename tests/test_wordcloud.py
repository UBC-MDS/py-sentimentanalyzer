from pysentimentanalyzer.generate_wordcloud import generate_wordcloud
import pandas as pd
import pytest



def test_wordcloud_valid_input():
    """Assert not passing a dataframe to the function"""
    with pytest.raises(TypeError):
        generate_wordcloud("not a dataframe", "col")

def test_wordcloud_none_df():
    """Assert not a None dataframe"""
    with pytest.raises(TypeError):
        generate_wordcloud(None, "col")

def test_wordcloud_none_col():
    """Assert not a None col"""
    df = pd.read_csv("test_tweets.csv")
    with pytest.raises(TypeError):
        generate_wordcloud(df, None)
    