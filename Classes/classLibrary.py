class crudCliente:
    def __init__(self):
        self.VetCli = []

    def display(self):
        print("\nBookstore Customers:")
        for i in self.VetCli:
            print(i)

    def add(self, client):
        self.VetCli.append(client)

class Library:
    def __init__(self, client, books, book_borrowing):
        self.client = client
        self.books = books
        self.book_borrowing = book_borrowing
    
    def library_client(self):
        print(f"{self.client} is a client in the library")

    def book(self):
        print(f"{self.client}, you have this book ({self.books})")

    def borrowing(self):
        print(f"{self.client}, you have this borrowing book ({self.book_borrowing})")


VetCli = crudCliente()

c1 = Library("Vitor", "Lord of the Rings", "Harry Potter")
c2 = Library("Andreia", "Harry Potter", "Lord of the Rings")

c1.library_client()
c2.library_client()
c1.book()
c2.book()
c1.borrowing()
c2.borrowing()


VetCli.add(c1.client)
VetCli.add(c2.client)

VetCli.display()