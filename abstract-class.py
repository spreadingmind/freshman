from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(self): pass


class MyBook(Book):
    def __init__(self, title,author, price):
        super().__init__(title,author)
        self.price = price
    def display(self):
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('Price: ', self.price)
# title=input()
# author=input()
# price=int(input())
title = 'Deep Work'
author = 'Cal Newport'
price = 100

new_novel = MyBook(title,author,price)
new_novel.display()
