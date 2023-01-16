import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
nltk.download("punkt")

def get_compound_score(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    return score["compound"]

def get_sentiment(text):
    score = get_compound_score(text)
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    return "neutral"

def get_sentiment_and_score(df, col):
    df = df.assign(compound_score=df[col].apply(get_compound_score))
    df = df.assign(sentiment=df[col].apply(get_sentiment))
    return df
