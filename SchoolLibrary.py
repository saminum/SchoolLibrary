import sys
import re
from Book import Book

class SchoolLibraryBookOrderer(object):

    def __init__(self):
        self.txtFileLocation = ''
        self.programRunning = True
        self.actions = {"1": self.addNewBook,
                   "2": self.dispayBooks,
                   "Q": self.exitProgram}
        self.books = []

    def startProgram(self):
        arguments = sys.argv[1:]
        if len(arguments) != 1:
            self.exitProgram("You are allowed to define only one txt file name. Exiting program")
        self.txtFileLocation = self.txtFileLocation+arguments[0]
        self.readTxtFile()
        self.sortBooks()
        self.dispayBooks()
        while(self.programRunning):
            self.showUserInterface()

    def readTxtFile(self):
        try:
            file = open(self.txtFileLocation, mode='r')
            for line in file:
                result = re.split('#', line.rstrip())
                b = Book(result[0], result[1], result[2])
                self.books.append(b)
            file.close()
        except IOError:
            self.exitProgram("Could not read txt file. Exiting program")

    def sortBooks(self):
        self.books = sorted(self.books, key=lambda x: x.bookWriter)

    def dispayBooks(self):
        for book in self.books:
            print(book.displayBook().title())

    def showUserInterface(self):
        print("What would you like to do?")
        print("1) Add new book")
        print("2) Print current database content in ascending order")
        print("Q) Exit the program")
        userInputValue = input("Give value")
        if(userInputValue not in ("1","2","Q")):
            print("Not valid value. Please try again.")
            self.showUserInterface()
        else:
            self.actions[userInputValue]()

    def updateTxtFile(self):
        file = open(self.txtFileLocation,mode='w')
        for book in self.books:
            file.write(book.getBook().title() + '\n')
        file.close()

    def addNewBook(self):
        bookName = input("Please give book's name")
        bookWriter = input("Please give book writer's name")
        bookIsbn = input("Please give book's ISBN")
        print("--"+ bookName + " " + bookWriter + " " + bookIsbn + "--")
        userInputValue = input("Is above correct (y=yes, any other=no)?")
        if(userInputValue=="y"):
            book = Book(bookName,bookWriter,bookIsbn)
            self.books.append(book)
            self.sortBooks()
            self.updateTxtFile()
        else:
            self.showUserInterface()

    def exitProgram(self, message='Exiting program'):
        print(message)
        exit(0)

if __name__ == '__main__':
    s = SchoolLibraryBookOrderer()
    s.startProgram()

