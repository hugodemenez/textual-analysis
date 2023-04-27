"""Module for the textual analysis of a text

using GPT-3.5-turbo model and Vader dictionnary based textual analysis.
"""

import os
import openai
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

EXAMPLES = [
    "Be extremely carefull with the extreme volatility on the markets.",
    "Spotted on the streets of Istanbul, Turkey, a country with 55%-80%+ inflation",
    """Some people said that closed APIs were winning...
    but we will never give up the fight for open source AI ⚔️⚔️
    Today is a big day as we launch the first open source alternative to ChatGPT:
    HuggingChat 💬
    Powered by Open Assistant's latest model 
    – the best open source chat model right now
    – and Hugging Face Inference API.
    """,
]

def get_sentiment_analysis_gpt(text):
    """This functions returns the sentiment analysis of a text using GPT-3.5-turbo model.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are the best algorithm to predict the sentiment of a text."
                    "Provide the same format for answers as the following example (don't give extras information):"
                )
            },
            {
                "role": "assistant",
                "content": (
                    "INPUT : The plot was good, but the characters are uncompelling and the dialog is not great.\n"
                    "OUTPUT :{'neg': 0.327, 'neu': 0.579, 'pos': 0.094, 'compound': -0.7042}"
                )
            },
            {
                "role": "user",
                "content": (
                    f"INPUT : {text}\n"
                    "OUTPUT : "
                )
            }
        ]
    )
    return response['choices'][0]['message']['content']


def get_sentiment_analysis_dictionnary(text):
    """This functions returns the sentiment analysis of a text 
    using Vader dictionnary based textual analysis.
    """
    analyzer = SentimentIntensityAnalyzer()
    return f"{str(analyzer.polarity_scores(text))}"

if __name__ == "__main__":
    load_dotenv()  # take environment variables from .env.
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # TEST = "Make sure you :) or :D today!"

    # # Comparing with Vader dictionnary based textual analysis
    # gpt_analysis = get_sentiment_analysis_gpt(TEST)
    # dictionnary_analysis = get_sentiment_analysis_dictionnary(TEST)

    # print(f"""
    #     Text : {TEST}

    #     // Results
    #     GPT : {gpt_analysis}
    #     Dictionnary : {dictionnary_analysis}
    # """)

    while True:
        user_input = input(
            "--- PRESS CTRL + C TO EXIT ---\n"
            "Enter a text to analyze : "
        )
        # Comparing with Vader dictionnary based textual analysis
        gpt_analysis = get_sentiment_analysis_gpt(user_input)
        dictionnary_analysis = get_sentiment_analysis_dictionnary(user_input)

        output = (
            "\n// Input\n"
            f"Text : {user_input}\n"
            "// Results\n"
            f"GPT : {gpt_analysis}\n"
            f"Dictionnary : {dictionnary_analysis}\n"
        )

        print(output)
