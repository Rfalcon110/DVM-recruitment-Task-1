
from library_management import Book,Shelf,User
from data import book_data
import logging
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


library=[]#placeholder for all the books
for book in book_data:#assigning class book to all the entries
    book_in_library=Book(book["name"],book["isbn"],book["author"])
    library.append(book_in_library)

library_shelf=[]#placeholder for shelves
genre=["action","adventure","romance","horror","mystery","motivational"]

for genre in genre:#assigning class shelf to all the entries
    genre1=Shelf(genre)
    library_shelf.append(genre1)


def add_book_in_shelf(input_genre,input_book_name):#adding a book to a shelf
    for genre in library_shelf:#to add a book
        if genre.genre==input_genre:
            for book in library:
                if book.name==input_book_name:
                    genre.add_book(book,user)
                

def remove_book_from_shelf(input_genre,input_book_name):#removing a book from shelf
    for genre in library_shelf:
        if genre.genre==input_genre:
            for book in genre.shelf:
                if book.name==input_book_name:
                    genre.remove_book(book,user)          


def print_catalog(input):#printing catalog
    for genre in library_shelf:
        if genre.genre==input:
            genre.show_catalog()
def populate_shelf(input_genre):
    for item in library_shelf:
        if input_genre==item.genre:
            item.populate_books()
    


def reserve(user):#reserve a book
    name=input("which book do u wish to reserve?")
    for book in library:
        if name==book.name:
            book.reserve_book()
            logging.info(f"{name} reserved by {user}")        

def return_book(user):#returning  a book
    name=input("which book do u wish to return?")
    for book in library:
        if name==book.name:
            book.return_book()
            logging.info(f"{name} returned by {user}")        
           


def borrow(user):#borrowing a book
    name=input("which book do u wish to borrow?")
    for book in library:
        if name==book.name:
            book.borrow_book(user)
            logging.info(f"{name} borrowed by {user}")        
        
def i_am_a_librarian():
        if user.access:
            print('''
                 1.populate books
                 2.check book status
                 3.add book to shelf
                 4.remove book from shelf
                 5.go back'''
                 )
            
            temp2=int(input("what do u wish to do?\n"))
            if temp2==1:
                populate=input("which shelf do u wish to populate?(the excel sheet should be in the directory named as \"book_populate\")\n")
                populate_shelf(populate)
            if temp2==2:
                book_name=input("enter the name of the book\n")
                for book in library:
                    if book_name==book.name:
                        print(book.owner)
            elif temp2==3:
                input_shelf_name=input('enter the shelf name\n')
                input_book_name=input("enter the book's name\n")
                add_book_in_shelf(input_shelf_name,input_book_name) 
            elif temp2==4:
                input_shelf_name=input('enter the shelf name\n')
                input_book_name=input("enter the book's name\n")
              
                remove_book_from_shelf(input_shelf_name,input_book_name)
            elif temp2==5:
                return
            
library_works=True
username=input("enter username(enter librarian if you are one)\n")
user=User(username)


while library_works:
    if user.name=="librarian":
        user.librarian()
    print('''
             1.borrow a book
             2.return a book
             3.reserve a book
             4.access a shelf
             5.i am a librarian
             6.exit''')
    temp=int(input("what do you wish to do?\n"))
    if temp==1:
        borrow(user.name)
    elif temp==2:
        return_book(user.name)
    elif temp==3:
        reserve(user.name)
    elif temp==4:
            for shelf in library_shelf:
                print(shelf.genre)
            input_shelf=input("which shelf do you wish to access?\n")               
            for item in library_shelf:
                if input_shelf==item.genre:
                    print(
'''
1.number of books
2.catalog of books''')
                    temp1=int(input("what do you wish to do?\n"))
                    if temp1==1:
                        item.give_book_count()
                    else:
                        item.show_catalog()
    elif temp==5:
       i_am_a_librarian()     
    elif temp==6:
        library_works=False
