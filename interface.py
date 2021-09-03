from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from search_stock import SearchStock
from search_news import SearchNews
import webbrowser

FONT = ('Courier', 20, 'bold')


class Interface:

    def __init__(self, search_stock: SearchStock, search_news: SearchNews):
        self.search_stock = search_stock
        self.search_news = search_news
        self.company = str
        self.window = Tk()
        self.window.config(padx=20, pady=20)
        self.window.title('Stock Thingy')

        # Title
        self.title = Label(text='Stock Thingy', font=FONT)
        self.title.grid(column=0, row=0, columnspan=3)

        # Company Label
        self.company_l = Label(text='Company to search: ')
        self.company_l.grid(column=0, row=1, pady=(20, 0))

        # Company Entry
        self.company_e = Entry()
        self.company_e.focus()
        self.company_e.grid(column=1, row=1, pady=(20, 0))

        # Company Search
        self.company_b = Button(text='Search', command=self.search)
        self.company_b.grid(column=2, row=1, pady=(20, 0), padx=(10, 10))

        # Stock Label
        self.stock_l = Label(text='Stock\'s symbol to get news: ')
        self.stock_l.grid(column=0, row=2, pady=(20, 0))

        # Stock Entry
        self.stock_e = Entry()
        self.stock_e.grid(column=1, row=2, pady=(20, 0))

        # Stock Button Get NEWS
        self.stock_news = Button(text='News', command=self.get_news)
        self.stock_news.grid(column=2, row=2, pady=(20, 0), padx=(10, 10))

        self.window.mainloop()

    def get_data(self):
        self.company = self.company_e.get()
        self.search_stock.get_data(self.company)

    def search(self):
        if self.company_e.get() == '':
            messagebox.showerror('Error', 'Blank entry!')
        else:
            def all_children():
                _list = new_window.winfo_children()
                for widget in _list:
                    widget.pack_forget()
                new_window.destroy()

            self.get_data()
            new_window = Toplevel(self.window, padx=20, pady=20)
            for item in self.search_stock.result:
                Label(new_window, text=f'Symbol: {item["symbol"]}').pack()
                Label(new_window, text=f'Company Name: {item["name"]}\n').pack()
            Button(new_window, text='Back', command=all_children).pack()

    def get_news(self):
        stock = self.stock_e.get()
        news_data = self.search_news.get_news(stock)
        if stock == '' or news_data == []:
            messagebox.showerror("Error", "That stock ain't exists!")
        else:
            new_window = Toplevel(self.window, pady=20, padx=20)
            for element in news_data:
                Label(new_window, text=f'\n{element["title"]}').pack()
                Button(new_window, text='Read on!', command=lambda: webbrowser.open(f'{element["article_url"]}')).pack()
