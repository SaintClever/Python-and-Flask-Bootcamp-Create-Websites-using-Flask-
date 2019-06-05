'''SPECIAL METHODS - Methpds that act upon built in data types
Ex. When len() method provides the lenght for an array or a string'''

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    # def __str__(self): # str representation
    #     # return 'YUP!'
    #     return f'Title: {self.title}, Author: {self.author}'

    # Special Method
    def __repr__(self): # str representation
        # return 'YUP!'
        return f'Title: {self.title}, Author: {self.author}'

    # Special Method
    def __len__(self): # length
        return self.pages


mybook = Book('Python Rocks!', 'Nesta', 250)
print(mybook)
length_book = len(mybook)
print(length_book)
