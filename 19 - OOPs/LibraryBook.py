# Problem 20: Create a LibraryBook class with title, author, and is_available. Create borrow_book(), return_book(), and display_status(). 
# Borrow only available books.

# Goal: Manage changing object state.

class LibraryBook:
    print("--------------- Book Details --------------------")
    def __init__(self,title:str,author:str,is_available:bool):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available == True:
            self.is_available = False
            print(f"The book {self.title} has been successfully borrowed.")
        else:
            print(f"Sorry, the book is not available.")

    def return_book(self):
        if not self.is_available:
            print(f"You have returned the {self.title} book successfully.")
        else:
            print("The book is already in the library.")

    def display_details(self):
        print(f"\nBook Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Availability: {self.is_available}")

book1 = LibraryBook("Freedom","Aryan",True)
book2 = LibraryBook("Mindset","Dr. Carol S. Dweck",False)

book1.display_details()
book1.borrow_book()
book1.return_book()

book2.display_details()
book2.borrow_book()
book2.return_book()