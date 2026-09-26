# Problem 17: Create a Book class with title, author, price, and pages.
# Create display_details(), apply_discount(percent), and display_price().
# The discount method must update price.
#
# Goal: Modify object state through methods.

class Book:
    print("------ Book Details ------")
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def display_details(self):
        print(f"\n------ {self.title} ------")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Pages: {self.pages}")

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        discounted_price = discount
        print(f"Discounted Price: {discounted_price}")

    def display_price(self):
        print(f"Price: {self.price}")

book1 = Book("Sabse Bada Khiladi", "Aryanbhau Patil", 2500, 250)
book2 = Book("Make Epic Money", "Ankoor Warikoo", 500, 300)
book3 = Book("Mindset", "Dr. Carol S. Dweck", 450, 350)
book1.display_details()
book1.apply_discount(50)
book2.display_details()
book2.apply_discount(50)
book3.display_details()
book3.apply_discount(50)