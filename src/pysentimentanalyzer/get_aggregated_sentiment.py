def aggregate_sentiment(df, col):
    """
    Returns an aggregated compound score representing sentiment: 
    -1 (most extreme negative) and +1 (most extreme positive). The compound score
     is a normalized score calculated by summing the valence scores of each word in the lexicon.

    Parameters:
    ------
    df : Pandas DataFrame
        DataFrame containing the reviews
    col: str
        Column name in the dataframe that contains the reviews 
    Returns:
    -------
    aggregated sentiment score of the text: (float)
     Examples
    --------
    >>> agg_score = aggregate_sentiment(df, "reviews")
    >>> agg_score
    0.81
    """
    pass