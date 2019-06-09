class Book(object):

    def __init__(self, bookName, bookWriter, bookIsdn):
        self.bookname = bookName.lower()
        self.bookWriter = bookWriter.lower()
        self.bookIsdn = bookIsdn.lower()

    def getBook(self):
        return self.bookname + '#' + self.bookWriter + '#' + self.bookIsdn

    def displayBook(self):
        return self.bookname + ' ' + self.bookWriter + ' ' + self.bookIsdn

    def getBookWriter(self):
        return self.bookWriter

