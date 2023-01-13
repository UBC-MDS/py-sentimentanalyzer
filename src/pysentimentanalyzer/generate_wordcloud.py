def generate_wordcloud(df):
    """
    Generate the word cloud from a given survey in the form of a 
    data frame and create a word cloud.

    Parameters
    ----------
    df : Pandas DataFrame
        DataFrame containing the survey comments 

    Returns
    -------
    WordCloud:
        A word cloud instance that can be later plotted or saved as an image

    Examples
    --------
    >>> wc = generate_wordcloud(df)
    >>> plt.imshow(wc, interpolation="bilinear")
    >>> plt.show()
    """
    pass