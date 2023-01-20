import pandas as pd
from pysentimentanalyzer.helper import *

def test_get_commpound_score():
    text = "I love my dogs!"
    assert get_compound_score(text) > 0, "Compound score should be greater than 0 (positive)."

def test_get_sentiment():
    text = "I love my dogs!"
    assert get_sentiment(text) == "positive", f"Sentiment should be positive for the text: {text}."

def test_get_sentiment_and_score():
    text_list = [
        "I love my dogs!",
        "This food tastes awful."
    ]
    df = pd.DataFrame({"text": text_list})
    df = get_sentiment_and_score(df, "text")
    assert "compound_score" in df.columns, "Returned DataFrame should contain column called compound_score."
    assert "sentiment" in df.columns, "Returned DataFrame should contain column called sentiment"
