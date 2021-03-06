#!/usr/bin/env python3
''' Object Oriented Programming
Implementation fo simple bookstore
Create methods for search_books( title or author

'''


class BookStore(object):

    def __init__(self):
        self.books = []
        self.authors = []

    def add_book(self, book_object):
        self.books.append(book_object)
        self.authors.append(book_object.author)

    def search_books(self, **kwargs):
        res = []
        if 'title' in kwargs:
            for book in self.books:
                if kwargs['title'] in book.title.lower():
                    res.append(book)
        elif 'author' in kwargs:
            for book in self.books:
                if kwargs['author'] in book.author.name.lower():
                    res.append(book)
        else:
            raise AttributeError()
        return res

class Author(object):
    authors = []
    def __init__(self, name=None, nationality=None):
        self.name = name
        self.nationality = nationality

class Book(object):
    books = []
    def __init__(self, title=None, author=None):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title


store = BookStore()

# Authors
poe = Author(name="Edgar Allan Poe", nationality="American")
doyle = Author(name="Arthur Conan Doyle", nationality='British')

# Books
raven = Book(title="The Raven", author=poe)
study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

# Adding books to instance of Bookstore called "store"
store.add_book(raven)
store.add_book(study_in_scarlet)

# results = store.search_books(title='raven')
results = store.search_books(author='doyle')
results = store.search_books(test='doyle')
print(results)
# print("Object raven: {}".format(results[0]))
