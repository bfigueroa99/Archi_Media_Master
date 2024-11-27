from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

sia = SentimentIntensityAnalyzer()

generator = pipeline('text-generation', model='gpt2')

def generate_content(title, content):
    prompt = f"Title: {title}\nContent: {content}\nGenerated Content:"
    generated = generator(prompt, max_length=200, num_return_sequences=1)
    return generated[0]['generated_text']