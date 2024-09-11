class Book:
 def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


# Usage
Book=Book("To Kill a Mockingbird", "Harper Lee", 281)
Book.display_details()