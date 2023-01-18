# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def sentiment_score_plot(df):
    """
    Creates and Saves to disk, a binned histogram showing count of reviews
    ranging from negative to positive sentiment score.
    
    Provides the most frequent sentiment score and the corresponding percentage

    Parameters
    ----------
    df : Pandas DataFrame
        DataFrame containing the reviews
    
    Returns
    -------
    Plot:
        A plot object

    Examples
    --------
    >>> plot = sentiment_score_plot(df, "reviews")
    >>> plt.show()
    """
    
    # Check the input dtypes
    assert isinstance(df, pd.DataFrame), "input should be type dataframe" 
    #assert isinstance(col, str), "column name should be string dtype" # TBD Print this out
    
    # Check that the column exists in dataframe
    assert "compound_score" in df.columns, "compuound score not computed in dataframe"
    
    # Check is any value in col is non-numeric
    assert all(df["compound_score"].map(np.isreal)), "Non numeric values computed as compound score, only numeric values expected"
        
    # Plot the figure
    fig_size = (7, 5)
    f = plt.figure(figsize=fig_size)
    
    ax = f.add_subplot(1,1,1)
    y, x, _ = plt.hist(df["compound_score"], density=False, bins=10, label = "Sentiment Counts")
    plt.legend(loc="upper right")
    plt.ylabel("Count")
    plt.xlabel("Sentiment Score range")
    plt.title("Distibution of Sentiments")
    
    # Uncheck below code if required to save plot to disk
    # plt.savefig('test_hist.png')
    # print("Plot saved to disk") 
    # print("="*100)
    # print("\n")
    
    # Histogram metrics
    max_counts = y.max()
    min_counts = y.min()
    max_percentage = max_counts/len(df["compound_score"])
    
    print(f"The highest frequency ({max_counts}) of sentiment scores are in range {x[y.argmax()]:.1f} to {x[y.argmax()+1]:.1f} which forms {max_percentage*100:.02f}% of samples in the dataset")
    
    return f