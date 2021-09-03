from interface import Interface
from search_stock import SearchStock
from search_news import SearchNews


search_stock = SearchStock()
search_news = SearchNews()
interface = Interface(search_stock, search_news)
