from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def generate_feedback(title, content):
    # Subscribe to the article content received from the Backend
    sentiment_score = sia.polarity_scores(content)['compound']
    
    if sentiment_score > 0:
        return f'The article "{title}" appears to be true based on the positive sentiment.'
    else:
        return f'The article "{title}" appears to be false based on the negative sentiment.'