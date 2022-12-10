class Book():
    usertype="basic_user"
       
    def __init__(self,name,isbn,author):
        self.name=name
        self.isbn=isbn
        self.author=author
        self.owner="library"
        
    def borrow_book(self,user):
        print(f"the book you wish to borrow is {self.name} isbn {self.isbn} author {self.author}")
        self.owner= user    
    
    def return_book(self):
        self.owner="library"

    def reserve_book(self):
        self.owner="reserved"


class Shelf():
    shelf=[]
    def __init__(self,genre):
        self.genre=genre
       
        self.book_count=len(self.shelf)
        
    def add_book(self,book,access):
        if access:
            self.shelf.append(book)
    def remove_book(self,book,access):
        if access:
            self.shelf.remove(book)
    def show_catalog(self):
        print(self.shelf)
    def give_book_count(self):
        print(len(self.shelf))
class User():
    def __init__(self,username):
        self.role='reader'
        self.access=False
        self.name=username
    def librarian(self):
        self.access=True    
    
            
    
    

    

    
    
    
    
        
        
