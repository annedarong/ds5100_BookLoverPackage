#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Course: DS 5100
Module: 09 Python Testing
Topic: HW 09 Unit Testing a Book Lover Class
Author: Anneda Rong 
Date: 05 Jul 2022
"""
import pandas as pd

class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name': [],'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        has_book = False #flag
        for index, rows in self.book_list.iterrows():
            if rows[0] == book_name:
                has_book = True #has_book gets flagged
                break
        if has_book == False:
            self.num_books += 1
            self.book_list.loc[len(self.book_list)] = [book_name, rating]
            
    def has_read(self, book_name):
        for index, rows in self.book_list.iterrows():
            if rows[0] == book_name:
                return True
        return False
    
    def num_books_read(self):
        return(self.num_books)

    def fav_books(self):
        favorite_books = []
        for index, rows in self.book_list.iterrows():
            if rows[1] > 3:
                favorite_books.append(rows[0])
        return(favorite_books)
            
#if __name__ == '__main__':
##    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
##    test_object.add_book("War of the Worlds", 4)
##    test_object.fav_books()
#    # And so forth
