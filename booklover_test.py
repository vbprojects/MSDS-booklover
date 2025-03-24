import unittest
from booklover import BookLover

# ## Task 2

# (6 points; 1 pt per method)

# Create a test suite for the previous class in a file named `booklover_test.py`.

# In the file, write a class called `BookLoverTestSuite`, being sure to import the `unittest` library and the BookLover class from the first file.

# ### Unit Tests

# In this class, include the unit tests below: 

# - `test_1_add_book()`: Add a book and test if it is in `book_list`.
# - `test_2_add_book()`: Add the same book twice. Test if it's in `book_list` only once.
# - `test_3_has_read()`: Pass a book in the list and test the answer is `True`.
# - `test_4_has_read()`: Pass a book NOT in the list and use `assert False` to test if the answer is `True`
# - `test_5_num_books_read()`: Add some books to the list, and test num_books matches expected.
# - `test_6_fav_books()`: Add some books with ratings to the list, making sure some of them have rating > 3. 
#   - Your test should check that the returned books have rating  > 3.

# Note that you do not need to create an `__init__()` method in this class, nor do you have to define any class variables.

# Instead, treat every method as a small, stand-alone program in which you create a new object for your test. This is not the best practice in a production environment, but it works and it will enable you to get the gist of unit testing. 

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        self.assertTrue((test_object.book_list['book_name'] == "War of the Worlds").sum() == 1)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        self.assertTrue((test_object.book_list['book_name'] == "War of the Worlds").sum() == 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        self.assertTrue(test_object.has_read("War of the Worlds"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        self.assertFalse(test_object.has_read("War and Peace"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War and Peace", 3)
        test_object.add_book("The Hobbit", 5)
        test_object.add_book("Wiley Calculus: Multivariable, 7th Edition", 1)
        self.assertTrue(test_object.num_books_read() == 4)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War and Peace", 3)
        test_object.add_book("The Hobbit", 5)
        test_object.add_book("Wiley Calculus: Multivariable, 7th Edition", 1)
        self.assertTrue(test_object.fav_books()['book_rating'].min() > 3)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
