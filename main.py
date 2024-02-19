class Library:                                                              #Creation of the class Library
    def __init__(self, file_name):
        self.file_name = file_name                                          #Creation the constructer method
        try:
            self.file = open(self.file_name, 'a+')                          #Open txt with a+ module
            self.file.seek(0)                                               #To go to the beginning of the file
        except FileNotFoundError:
            print("File '{}' not found.".format(self.file_name))            #File not found error check

    def __del__(self):                                                       #Creation the destructer method
        if hasattr(self, 'file'):
            self.file.close()
            print("File '{}' has been closed.".format(self.file_name))

    def list_books(self):                                                     #Listing function
        self.file.seek(0)
        books = self.file.readlines()                                         #Reading the information in the file line by line
        if books:
            print("***** Books in the Library *****")
            for book in books:
                title, author, _, _ = book.strip().split(',')                 #Using Split to retrieve only book title and author name
                print("Title: {}, Author: {}".format(title, author))          #Printing two information on the screen
        else:
            print("There are no books in the library.")                       #Message to show when there are no books in the library

    def add_book(self):                                                       #Adding function
        title = input("Enter the title of the book: ")                        #Receiving inputs from the user
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")

        self.file.seek(0)                                                      #Checking whether the book has
        books = self.file.readlines()                                           #been added to the library before
        for book in books:
            if title in book:                                                          #If the book is already in the library,
                print("The book '{}' already exists in the library.".format(title))     #it will not be added again
                return

        book_info = "{},{},{},{}\n".format(title, author, release_year, num_pages)    #If the book is not in the library, add it
        self.file.write(book_info)                                                    #The added book is added to the file
        print("The book '{}' has been added to the library.".format(title))

    def remove_book(self):                                                            #Removing function
        title_to_remove = input("Enter the title of the book to remove: ")            #Taking the name of the book to be
        self.file.seek(0)                                                               #removed as input from the user
        books = self.file.readlines()
        updated_books = []                                                        #List created to add books that will not be removed
        found = False
        for book in books:                                                        #Searching for book title and checking
            book_info = book.strip().split(',')
            if title_to_remove.lower() in book_info[0].lower():
                found = True
            else:                                                                 #Appending unmatched books to the list
                updated_books.append(book)

        if found:
            self.file.seek(0)                                                     #If a book is found, its removal process
            self.file.truncate(0)
            self.file.writelines(updated_books)
            print("The book '{}' has been removed from the library.".format(title_to_remove))
        else:
            print("The book '{}' was not found in the library.".format(title_to_remove))    #Message to be given if the book
                                                                                            #to be removed is not in the library

    def search_book(self, title):                                           #Search function by book name
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        for book in books:                                                  #Loop comparing book names
            if title.lower() in book.lower():
                print(book.strip())
                found = True                                                #Returns True if the book is in the library
                break
        if not found:
            add_book_choice = input(                  #If the book we are looking for is not in the library, it asks if we want to add that book
                "The book '{}' is not found in the library. Do you want to add it? (Yes/No): ".format(title))
            if add_book_choice.lower() == 'yes':      #If the answer is yes, a new book adding function is called
                self.add_book_interactively()

    def add_book_interactively(self):                               #Here, the user is asked for information about the book
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")
        self.add_book_after_search(title, author, release_year, num_pages)   #And this information is sent to the add function

    def add_book_after_search(self, title, author, release_year, num_pages):   #Its parameters are different compared to other adding functions
        book_info = "{},{},{},{}\n".format(title, author, release_year, num_pages)
        self.file.write(book_info)                                                  #And the new book is added to the library
        print("The book '{}' has been added to the library.".format(title))

    def search_author(self, author):                                        #Author name search function
        self.file.seek(0)                                                   #The author's name is searched and all books
        books = self.file.readlines()                                        #by that author are displayed
        found = False
        for book in books:
            book_info = book.strip().split(',')
            if author.lower() in book_info[1].lower():
                print(book.strip())
                found = True
        if not found:                                                          #The message shown if there is no book by that author
            print("No books found for author '{}' in the library.".format(author))


def main():                                                 #Main
    lib = Library("books.txt")                              #Create an object named “lib” with “Library” class

    while True:                                             #Creating a menu
        print("\n*** MENU ***")
        print("1) List Books")                              #List function
        print("2) Add Book")                                #Add function
        print("3) Remove Book")                             #Remove function
        print("4) Search Book")                             #Search Book Function
        print("5) Search Author")                           #Search Author Function
        print("6) Exit")                                    #Exit

        choice = input("Enter your choice: ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':                                 #Input requested for searches
            title = input("Enter the title of the book: ")
            lib.search_book(title)
        elif choice == '5':                                 #Input requested for searches
            author = input("Enter the name of the author: ")
            lib.search_author(author)
        elif choice == '6':
            print("Exiting...")
            break
        else:                                                #Entering a different input
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
