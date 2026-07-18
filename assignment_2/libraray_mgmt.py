class book:
    def __init__ (self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return f"Title:{self.title}, Author: {self.author}"

class Library:
    def __init__(self):
        self.books=[]

    def addBook(self,title,author):
        Book= book(title,author)
        self.books.append(Book)
        print("book added")


    def removeBook(self,title):
        for book in self.books:
            self.books.remove(book)
            print("book removed")
            return
        
    def searchBook(self,word):
        found=False
        for book in self.books:
            if(word.lower() in book.title.lower() or word.lower() in book.author.lower()):
                print(book)
                found=True

        if not found:
            print("no matching books found")



    def displayBooks(self):
        if len(self.books)==0:
            print("library is empty")
        else:
            for book in self.books:
                print(book)

library=Library()

while True:
    print("1. Add Book")
    print("2.Remove Book")
    print("3.Search Book")
    print("4.Display All Books")
    print("5. Exit")

    choice = input("Enter your choice")
    
    if choice == "1":
        title= input("Enter book title: ")
        author= input("Enter author name: ")
        library.addBook(title,author)

    elif choice == "2":
        title = input("enter book title")
        library.removeBook(title)

    elif choice == "3":
        word = input("enter title or author to search")
        library.searchBook(word)
    
    elif choice == "4":
        library.displayBooks()

    elif choice == "5":
        break

    else:
        print("Invalid choice")