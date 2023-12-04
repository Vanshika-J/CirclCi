import requests

def get_latest_news():
    api_key = '0aade89dc52f498da7828b05f8cc6dc1'
    endpoint = 'https://newsapi.org/v2/everything?q=tesla&from=2023-11-01&sortBy=publishedAt&apiKey=0aade89dc52f498da7828b05f8cc6dc1'
    
    response = requests.get(endpoint)
    if response.status_code == 200:
        articles = response.json()['articles']
        for article in articles:
            title = article['title']
            description = article['description']
            url = article['url']
            print(f"Title: {title}\nDescription: {description}\nRead more: {url}\n")

get_latest_news()
