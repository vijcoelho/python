class Library:
    def __init__(self, client, books, book_borrowing):
        self.client = client
        self.books = books
        self.book_borrowing = book_borrowing
    
    def library_client(self):
        print(f"{self.client} is client in the library")

    def book(self):
        print(f"{self.client}, you have this book ({self.books})")

    def borrowing(self):
        print(f"{self.client}, you have this borrowing book ({self.book_borrowing})")

c1 = Library("Vitor", "Lord of the rings", "Harry Potter")
c2 = Library("Andreia", "Harry Potter","Lord of the rings")

c1.library_client()
print("\n")
c2.library_client()
print("\n")
c1.book()
print("\n")
c2.book()
print("\n")
c1.borrowing()
print("\n")
c2.borrowing()








