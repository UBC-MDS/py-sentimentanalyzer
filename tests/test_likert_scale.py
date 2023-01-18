import pytest
import pandas as pd
from pysentimentanalyzer.likert_scale import convert_to_likert


sample_text = [
    "He is so fun and entertaining.",
    "He makes lectures very interesting"
]
df = pd.DataFrame({"text": sample_text})

def test_convert_to_likert():
    """Assert function returns a string and an integer"""
    description, value = convert_to_likert(df, "text")
    assert isinstance(description, str), "The first value returned should be a string."
    assert isinstance(value, int), "The second value returned should be an integer."
    assert int in [1, 2, 3, 4, 5], "The likert scale value should be either 1, 2, 3, 4 or 5."

def test_convert_to_likert_no_df():
    """Assert not passing in a DataFrame in the first parameter raises an exception"""
    with pytest.raises(Exception):
        convert_to_likert("not a dataframe", "col")

def test_convert_to_likert_no_col():
    """Assert not passing a valid column name in the second parameter raises an exception"""
    with pytest.raises(Exception):
        convert_to_likert(df, "123")
