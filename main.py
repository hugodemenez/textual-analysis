import openai
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are the best algorithm to predict the sentiment of a text."},
            {"role": "user", "content": "The plot was good, but the characters are uncompelling and the dialog is not great."},
            {"role": "assistant", "content": "The plot was good, but the characters are uncompelling and the dialog is not great. {'neg': 0.327, 'neu': 0.579, 'pos': 0.094, 'compound': -0.7042}"},
            {"role": "user", "content": "Make sure you :) or :D today!"}
        ]
    )

print(response)
print(response['choices'][0]['message']['content'])



# Comparing with Vader dictionnary based textual analysis


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from vaderSentiment import SentimentIntensityAnalyzer

sentences = [
    "Make sure you :) or :D today!", # mixed negation sentence
]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print(f"{sentence} {str(vs)}")
