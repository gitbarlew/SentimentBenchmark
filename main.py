import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from openai import OpenAI
import time
import openpyxl

nltk.download('vader_lexicon')
client = OpenAI(api_key='put_your_openAI_API_Key_here',
                organization='configure_organization_if_applicable', )


def analyze_sentiment_nltk(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)['compound']
    return 'positive' if score > 0.1 else 'negative' if score < -0.1 else 'neutral'


def analyze_sentiment_textblob(text):
    score = TextBlob(text).sentiment.polarity
    return 'positive' if score > 0.1 else 'negative' if score < -0.1 else 'neutral'


def analyze_sentiment_openai3(text):

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'You will be provided with a text, and your task is '
                           'to classify its sentiment as positive, neutral, or negative. '
                           'Data might not have been cleand up, '
                           ' and can contain empty responses or non-alphanumeric characters. If you are not able'
                           ' to ascertain the sentiment return Unknown.'
                           ' Respond only with one of the values: '
                           ' Postive, Negative, Neutral or Unknown.'
            },
            {
                'role': 'user',
                'content': str(text)}
        ],
    )
    sentiment = response.choices[0].message.content
    return sentiment


def analyze_sentiment_openai4(text):

    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {
                'role': 'system',
                'content': 'You will be provided with a text, and your task is '
                           'to classify its sentiment as positive, neutral, or negative. '
                           'Data might not have been cleand up, '
                           ' and can contain empty responses or non-alphanumeric characters. If you are not able'
                           ' to ascertain the sentiment return Unknown.'
                           ' Respond only with one of the values: '
                           ' Postive, Negative, Neutral or Unknown.'
            },
            {
                'role': 'user',
                'content': str(text)}
        ],
    )
    sentiment = response.choices[0].message.content
    return sentiment


def analyze_sentiment_openai4finetuned(text):

    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {
                'role': 'system',
                'content': 'You will be provided with a text, and your task is '
                           'to classify its sentiment as positive, neutral, or negative. '
                           'Data might not have been cleand up, '
                           ' and can contain empty responses or non-alphanumeric characters. If you are not able'
                           ' to ascertain the sentiment return Unknown.'
                           ' Respond only with one of the values: '
                           ' Postive, Negative, Neutral or Unknown.'
            },
            {
                'role': 'user',
                'content': str(text)}
        ],
        temperature=0.3,
        max_tokens=32,
        top_p=0.8
    )
    sentiment = response.choices[0].message.content
    return sentiment


def analyze_sentiment_openai3finetuned(text):

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'You will be provided with a text, and your task is '
                           'to classify its sentiment as positive, neutral, or negative. '
                           'Data might not have been cleand up, '
                           ' and can contain empty responses or non-alphanumeric characters. If you are not able'
                           ' to ascertain the sentiment return Unknown.'
                           ' Respond only with one of the values: '
                           ' Postive, Negative, Neutral or Unknown.'
            },
            {
                'role': 'user',
                'content': str(text)}
        ],
        temperature=0.3,
        max_tokens=32,
        top_p=0.8
    )
    sentiment = response.choices[0].message.content
    return sentiment


# Load data from Excel - change filename & sheet name to match your input document
df = pd.read_excel('input.xlsx', sheet_name='Sheet1')
# Provide name of the column containing data to analyze.
column_name = 'Can you explain your answer?'

start_time1 = time.time()
df['NLTK_Sentiment'] = df[column_name].astype(str).apply(analyze_sentiment_nltk)
print("--- %s seconds ---" % (time.time() - start_time1))

start_time2 = time.time()
df['TextBlob_Sentiment'] = df[column_name].astype(str).apply(analyze_sentiment_textblob)
print("--- %s seconds ---" % (time.time() - start_time2))

start_time3 = time.time()
df['ChatGPT3.5'] = df[column_name].astype(str).apply(analyze_sentiment_openai3)
print("--- %s seconds ---" % (time.time() - start_time3))

start_time4 = time.time()
df['ChatGPT3.5-finetuned'] = df[column_name].astype(str).apply(analyze_sentiment_openai3finetuned)
print("--- %s seconds ---" % (time.time() - start_time4))

start_time5 = time.time()
df['ChatGPT4.5'] = df[column_name].astype(str).apply(analyze_sentiment_openai4)
print("--- %s seconds ---" % (time.time() - start_time5))

start_time6 = time.time()
df['ChatGPT4.5-finetuned'] = df[column_name].astype(str).apply(analyze_sentiment_openai4finetuned)
print("--- %s seconds ---" % (time.time() - start_time6))


# Write results to a new Excel file
df.to_excel('benchmark_results.xlsx', index=False)
