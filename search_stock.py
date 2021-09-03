import os
import requests


class SearchStock:

    def __init__(self):
        self.AV_API_KEY = os.environ.get('AV_API_KEY')
        self.AV_END_POINT = 'https://www.alphavantage.co/query'
        self.av_parameters = {
            'function': 'SYMBOL_SEARCH',
            'keywords': str,
            'apikey': os.environ.get('AV_API_KEY')
        }
        self.result = []

    def get_data(self, keyword):
        self.result = []
        self.av_parameters['keywords'] = keyword.lower()
        response = requests.get(self.AV_END_POINT, self.av_parameters)
        response.raise_for_status()
        data = response.json()['bestMatches']

        for item in data:
            element = {
                'symbol': item['1. symbol'],
                'name': item['2. name']
            }
            self.result.append(element)
