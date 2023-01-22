from pysentimentanalyzer.get_aggregated_sentiment_score import aggregate_sentiment_score
import pandas as pd

sample_text = [
    "He is so fun and entertaining.",
    "He makes lectures very interesting"
]

df = pd.DataFrame({"text": sample_text})

def test_convert_to_aggregated_compound_score():
    """Assert function returns a float value"""
    float_output = aggregate_sentiment_score(df, 'text')
    assert isinstance(float_output, float), "The output should be a float."

def test_convert_to_pos_aggregated_compound_score():
    """Assert function returns a positive value"""
    positive_output = aggregate_sentiment_score(df, 'text')
    assert positive_output > 0, 'Output should be positive'

def test_aggregated_sentiment_score_output_value():
    """Checking the output of get_aggregated_sentiment_score"""
    output_value = aggregate_sentiment_score(df, 'text')
    assert output_value == 0.635, 'Output value should be same'

def test_convert_to_aggregated_compound_score_no_df():
    """Assert not passing in a DataFrame in the first parameter raises an exception"""
    with pytest.raises(Exception):
        aggregate_sentiment_score("not a dataframe", "col")

def test_convert_to_aggregated_compound_score_no_col():
    """Assert not passing a valid column name in the second parameter raises an exception"""
    with pytest.raises(Exception):
        aggregate_sentiment_score(df, "123")