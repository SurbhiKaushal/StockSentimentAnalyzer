from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    """
    Analyze sentiment of given text using VADER.
    Returns 'Positive', 'Negative', or 'Neutral'.
    """
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return "Positive 😀"
    elif compound <= -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"
