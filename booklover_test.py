#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Course: DS 5100
Module: 09 Python Testing
Topic: HW 09 Unit Testing a Book Lover Class
Author: Anneda Rong 
Date: 05 Jul 2022
"""

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        self.test_object.add_book('Harry Potter', 5)
        should_be_true = self.test_object.has_read('Harry Potter')
        self.assertTrue(should_be_true)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        before = self.test_object.num_books_read()
        self.test_object.add_book('Harry Potter', 5)
        after = self.test_object.num_books_read()
        self.assertEqual(before, after)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        when_true = self.test_object.has_read('Harry Potter')
        self.assertTrue(when_true)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        when_false = self.test_object.has_read('Fantastic Beasts')
        self.assertFalse(when_false)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        self.test_object.add_book('The Giving Tree', 5)
        self.test_object.add_book('To Kill a Mockingbird', 3)
        self.test_object.add_book('The Cat in the Hat', 4)
        self.test_object.add_book('Diary of a Wimpy Kid', 1)
        self.assertEqual(self.test_object.num_books_read(), 5)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        favorite_books = self.test_object.fav_books()
        expected_books = ['Harry Potter', 'The Giving Tree', 'The Cat in the Hat']
        self.assertEqual(favorite_books, expected_books)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)

