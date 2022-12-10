
from library_management import Book,Shelf,User
#from data import book_data
book_data=[{"name":"rich dad poor dad",
            "isbn":9876543,
            "author":"raunak"},
           {'name':'qwerty',
            'isbn':987241,
            'author':'xyz'},
           {'name':'asdf',
            'isbn':12387,
            'author':'lkjh'}]

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



def reserve():#reserve a book
    name=input("which book do u wish to reserve?")
    for book in library:
        if name==book.name:
            book.reserve_book()
            

def return_book():#returning  a book
    name=input("which book do u wish to return?")
    for book in library:
        if name==book.name:
            book.return_book()
            
def borrow(user1):#borrowing a book
    name=input("which book do u wish to borrow?")
    for book in library:
        if name==book.name:
            book.borrow_book(user1)
            

            
            
library_works=True
while library_works:
    
    username=input("enter username\n")
    user=User(username)
    if user.name=="librarian":
        user.librarian()
    print('''
             1.borrow a book
             2.return a book
             3.reserve a book
             4.access a shelf
             5.i am a librarian
             6.exit''')
    temp=int(input("what do u wish to do?\n"))
    if temp==1:
        borrow(user.name)
    elif temp==2:
        return_book()
    elif temp==3:
        reserve()
    elif temp==4:
            for shelf in library_shelf:
                print(shelf.genre)
            input_shelf=input("which shelf do wish to access enter 0 to go back\n")
            #if input_shelf="0":
#TODO go back                
            for item in library_shelf:
                if input_shelf==item.genre:
                    print('''1.number of books
                          2.catalog of books''')
                    temp1=int(input("what do wish to do?\n"))
                    if temp1==1:
                        item.give_book_count()
                    elif temp==2:
                        item.show_catalog()
    elif temp==5:
        if user.access:
            print('''1.populate books
                 2.check book status
                 3.add book to shelf
                 4.remove book from shelf
                 5.go back''')
            temp2=int(input("what do u wish to do?\n"))
#TODO populate books
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
        else:
            print("access denied")
    elif temp==6:
        library_works=False
#TODO exit