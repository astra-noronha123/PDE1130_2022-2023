#Author:Astra Noronha
#Msis number:M00909675
#Mini-Project:SOB 28,29,30
#this program is a book library, where the user can search for books, add new books and delete books
#random books added for testing
books = ["lord of the rings","pride and prejudice","little women","the great gatsaby","frankenstien"]
authors = ["j.r.r. tolkien", "jane auesten","louisa may alcott","f. scott fitzgerald","mary shelly"]

#Search by Title functions
def searchlibraybytitle(bookname):
    global booklistlength,authorlistlength
    #this function searches for books within the database by the book title and returns a single book
    found = False
    count = 0
    while found == False or count < booklistlength:
        if books[count] == bookname:
            print("The book is in the library")
            return books[count],authors[count]
            found = True
        else:
            count = count +1
    if found == False:
        print("The book is not in the library")

def searchlibraybyauthor(authorname):
    global booklistlength,authorlistlength
    #this function searches for books within the database by the author name and returns a single book
    found = False
    count = 0
    while found == False or count < authorlistlength:
        if authors[count] == authorname:
            print("The book is in the library")
            return books[count],authors[count]
            found = True
        else:
            count = count +1
    if found == False:
        print("The book is not in the library")

#an add book function, it adds to the end of the list
def addbook(bookname,bookauthor):
    global booklistlength,authorlistlength
    books.append(bookname)
    authors.append(bookauthor)
    booklistlength =+ 1
    authorlistlength =+ 1
    print("The book was added to the library")

#delete book function, it deletes a book by checking if its in the library
def deletebook(bookname,bookauthor):
    global booklistlength,authorlistlength
    if (bookname in books) and (bookauthor in authors):
        books.remove(bookname)
        books.remove(bookauthor)
        booklistlength =- 1
        authorlistlength =- 1
        print('The book is removed from the library')
    else:
        print("The book already isn't in the library")

#this function has an error when a new book is added? it does not display the rest of the list outside of the first item?
def displaybooks():
    global booklistlength,authorlistlength
    print(books,"\n",authors)
            
#-----------------------------------------------------------------------------------------------
#main program
#The menu and choice options are displayed, and the user can make a decision for as long as they run the program
booklistlength = len(books)
authorlistlength = len(authors)
continueprogram = input("Do you want to start the program?")
while continueprogram == 'y' or continueprogram == 'Y':
    choice = int(input("Menu options:\n 1:Search book by title \n2:Search book by author\n3:Add new book by title \n4:Delete a book\n5:Display all books in library\n"))
    if choice == 1:
        userin = input("Enter the book you are looking for:\n")
        book01 = searchlibraybytitle(userin)
        print(book01)
    elif choice ==2:
        userin06 = input("Enter the author to find their book:\n")
        author01 = searchlibraybyauthor(userin06)
        print(author01)
    elif choice ==3:
        userin02 = input("Enter a book you want to add:\n")
        userin04 = input("Enter the authors name:\n")
        addbook(userin02,userin04)
    elif choice ==4:
        userin03 = input("Enter a book you want to delete:\n")
        userin05 = input("Enter the authors name:\n")
        deletebook(userin03,userin05)
    elif choice ==5:
        displaybooks()   
    else:
        print("error, invalid choice")
    continueprogram = input("Do you want to continue the program? y/n:\n")
#choice 5 displays all the books in the library





