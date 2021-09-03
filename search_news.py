import os
import requests

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
NEWS_END_POINT = 'https://api.polygon.io/v2/reference/news'


class SearchNews:

    def __init__(self):
        self.news_parameters = {
            'apikey': NEWS_API_KEY,
            'limit': 3,
            'order': 'descending',
            'sort': 'published_utc'
        }

    def get_news(self, stock):
        self.news_parameters['ticker'] = stock
        news_response = requests.get(url=NEWS_END_POINT, params=self.news_parameters)
        news_response.raise_for_status()

        return news_response.json()['results']
