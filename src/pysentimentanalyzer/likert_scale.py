from get_aggregated_sentiment_score import get_aggregated_sentiment_score

def convert_to_likert(df, col):
    """Convert the sentiment scores to a likert scale from 1-7
    
    Parameters
    ----------
    df : Pandas DataFrame
        DataFrame containing the text to perform sentiment analysis
    col : string
        Name of the column of text in the Dataframe

    Returns
    -------
    string:
        description of the likert scale value
    int:
        likert scale value
        
    Examples
    --------
    >>> convert_to_likert(counts)
    """
    agg_score = get_aggregated_sentiment_score(df, col)
    if agg_score >= -1 and agg_score < -0.6:
        return "very negative", 1
    elif agg_score >= -0.6 and agg_score < -0.2:
        return "negative", 2
    elif agg_score >= -0.2 and agg_score <= 0.2:
        return "neutral", 3
    elif agg_score > 0.2 and agg_score <= 0.6:
        return "positive", 4
    elif agg_score >0.6 and agg_score <= 1:
        return "very positive", 5
    else:
        raise Exception("Aggregate compound score not in the valid range.")
    