# ## Task 1

# (5 points; .5 pt per attribute and method)

# Create a BookLover class in a file named `booklover.py`.

# ### Attributes

# |Attribute | Value |
# |----------|-------|
# | `name` | The name of the person (type:string) |
# | `email` | The person’s email, serving as a unique identifier (type:string) |
# | `fav_genre` | The person’s favorite book genre (e.g., mystery, fantasy, or historical fiction).  (type:string) |
# | `num_books` | Keeps track of the number of books the person has read (type:int) |
# | `book_list` | a dataframe with the columns `['book_name', 'book_rating']`

# The columns in `book_list` have the following meanings:
# - `book_name` is the title of the book the person has read.
# - `book_rating` is the person’s rating of that book on a scale of 1 to 5, where 1 means the person did not like the book at all, and 5 means the person loved the book. 

# Some example book entries are:

# ```python
# ("Jane Eyre", 4)
# ("Fight Club", 3)
# ("The Divine Comedy", 5)
# ("The Popol Vuh", 5)
# ```

# ```python
#   num_books = 0
#   book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
# ```
# Do not add any additional fields of your own.

# **Method 1:**



# ```python
# new_book = pd.DataFrame({
#     'book_name': [book_name], 
#     'book_rating': [book_rating]
# })

# self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
# ```

# Of course, be sure to see if `book_name` is not in the book list.

# **Method 2:**



# **Method 3:**



# **Method 4:**



# NOTE: The methods listed above do not have `self` as their first argument, but they should in your class.
import pandas as pd

class BookLover():
    # **Initializer:**
    # `__init__()`:
    # - `name`, `email`, and `fav_genre` (in this order) are required. 
    # - `num_books` and `book_list` are optional.
    # - Use these default parameters: 
    def __init__(self, name : str, email : str, fav_genre : str, num_books : int = 0, book_list : pd.DataFrame = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    # `add_book(book_name, rating)`:
    # - This function takes a `book name` (string) and `rating` (integer from 0 to 5)
    # - It tries to add the book to `book_list`. See hint below on how to pass a new book to the dataframe.
    # - Only add a book to the person’s `book_list` if that book doesn’t already exist.
    #   - It is sufficient to match on `book_name`.
    # - If it does exist, tell the user.
    # Hint: To add a new book to the book list (which is a dataframe), do this in your method, where `book_name` and `book_rating` are the arguments passed to the method.:
    # ```python
    # new_book = pd.DataFrame({
    #     'book_name': [book_name], 
    #     'book_rating': [book_rating]
    # })

    # self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    # ```
    def add_book(self, book_name: str, book_rating: int):
        if isinstance(book_name, str) and isinstance(book_rating, int) and (0 <= book_rating <= 5):
            if not self.has_read(book_name):
                new_book = pd.DataFrame({
                    'book_name': [book_name], 
                    'book_rating': [book_rating]
                })
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            else:
                print(f"{book_name} is already in the book list.")
        else:
            print("Please enter a valid book name and rating.")
    # `has_read(book_name)`
    # - This function takes `book_name` (string) as input and determines if the person has read the book.
    #   - That is, if that `book name` is in `book_list`. 
    #   - Again, it is sufficient to match on `book_name`.
    # - The method should return `True` if the person has read the book, `False` otherwise.
    def has_read(self, book_name: str):
        if isinstance(book_name, str) and (book_name in self.book_list['book_name'].tolist()):
            return True
        else:
            return False
    # `num_books_read()`
    # - This function takes no parameters and just returns the total number of books the person has read.
    def num_books_read(self):
        return len(self.book_list)
    # `fav_books()`:
    # - This function takes no parameters and returns the filtered dataframe of the person’s most favorite books. 
    # - Books in this list should have a rating > 3.
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
            
    
if __name__ == "__main__":
    
    # **Once you have created your class**

    # Be sure to instantiate your class to see if everything is working. You can do this by prototyping your class in a notebook, where you can run code that uses it there, and then save the class to the `.py` file when you are done. 

    # Or you can create a another file, say `demo.py` that imports and uses the class.

    # A final option -- which the test file will use -- is to put this code at the bottom of your `.py` file, after and outside of your class definition:

    # ```python

    # if __name__ == '__main__':
        
    #     test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    #     test_object.add_book("War of the Worlds", 4)
    #     # And so forth

    # ```
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    print(test_object.has_read("War of the Worlds"))
    print(test_object.num_books_read())
    test_object.add_book("War of the Worlds", 4)
    print(test_object.num_books_read())
