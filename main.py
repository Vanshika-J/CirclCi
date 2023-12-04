"""
Module to retrieve the latest news about Tesla from the News API.
"""
import requests


def get_latest_news():
    """
    Retrieve the latest news about Tesla from the News API.

    This function makes a request to the News
    API to fetch the latest news articles
    related to Tesla. It prints the title,
    description, and URL of each article.
    """
    endpoint = (
        "https://newsapi.org/v2/everything?q=tesla"
        "&from=2023-11-01&sortBy=publishedAt"
        "&apiKey=0aade89dc52f498da7828b05f8cc6dc1"
    )

    response = requests.get(endpoint, timeout=10)
    if response.status_code == 200:
        articles = response.json()["articles"]
        for article in articles:
            title = article["title"]
            description = article["description"]
            print(f"Title: {title}\nDescription: {description}")


get_latest_news()
