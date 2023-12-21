import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from openai import OpenAI
import time
import openpyxl

nltk.download('vader_lexicon')
client = OpenAI(api_key='OPENAI_API_KEY_GOES_HERE',
                organization='CONFIGURE_ORGANIZATION_IF_NEEDED', )


# Load data from Excel - specify filename & sheet name to match your input document
df = pd.read_excel('input.xlsx', sheet_name='Sheet1')

# Specify the column name containing text data for analysis
column_name = 'TextColumn'


def analyze_sentiment_nltk(text):
    """
    Analyze sentiment using NLTK's Sentiment Intensity Analyzer & Vader Lexicon.
    """
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)['compound']
    return 'Positive' if score > 0.1 else 'Negative' if score < -0.1 else 'Neutral'


def analyze_sentiment_textblob(text):
    """
    Analyze sentiment using TextBlob.
    """
    score = TextBlob(text).sentiment.polarity
    return 'Positive' if score > 0.1 else 'Negative' if score < -0.1 else 'Neutral'


def analyze_sentiment_openai(model, text, temperature=1.0, max_tokens=100, top_p=1.0):
    """
    Analyze sentiment using OpenAI's GPT models.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                'role': 'system',
                'content': ('You will be provided with a text, and your task is '
                            'to classify its sentiment as positive, neutral, or negative. '
                            'Data might not have been cleaned up, '
                            'and can contain empty responses or non-alphanumeric characters. '
                            'If you are not able to ascertain the sentiment, return Unknown. '
                            'Respond only with one of the values: '
                            'Positive, Negative, Neutral, or Unknown.')
            },
            {
                'role': 'user',
                'content': str(text)
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p
    )
    return response.choices[0].message.content


# Apply sentiment analysis functions to the specified column and measure execution time
start_time = time.time()
df['NLTK_Sentiment'] = df[column_name].astype(str).apply(analyze_sentiment_nltk)
print(f"NLTK Analysis Time: {time.time() - start_time} seconds")

start_time = time.time()
df['TextBlob_Sentiment'] = df[column_name].astype(str).apply(analyze_sentiment_textblob)
print(f"TextBlob Analysis Time: {time.time() - start_time} seconds")

start_time = time.time()
df['ChatGPT3.5'] = df[column_name].astype(str).apply(lambda x: analyze_sentiment_openai('gpt-3.5-turbo', x))
print(f"ChatGPT 3.5 Analysis Time: {time.time() - start_time} seconds")

start_time = time.time()
df['ChatGPT3.5-finetuned'] = df[column_name].astype(str).apply(lambda x: analyze_sentiment_openai('gpt-3.5-turbo', x, temperature=0.3, max_tokens=32, top_p=0.8))
print(f"ChatGPT 3.5 Finetuned Analysis Time: {time.time() - start_time} seconds")

start_time = time.time()
df['ChatGPT4'] = df[column_name].astype(str).apply(lambda x: analyze_sentiment_openai('gpt-4', x))
print(f"ChatGPT 4 Analysis Time: {time.time() - start_time} seconds")

start_time = time.time()
df['ChatGPT4-finetuned'] = df[column_name].astype(str).apply(lambda x: analyze_sentiment_openai('gpt-4', x, temperature=0.3, max_tokens=32, top_p=0.8))
print(f"ChatGPT 4 Finetuned Analysis Time: {time.time() - start_time} seconds")

# Write results to a new Excel file
df.to_excel('benchmark_results_new.xlsx', index=False)
