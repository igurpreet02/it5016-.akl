class Book:
    def __init__(self, title, author, publicationyear):
        self.title = title
        self.author = author
        self.publicationyear = publicationyear
        self.availability_status = True
    
    def mark_as_rented(self):
        self.availability_status = False

    def mark_as_available(self):
        self.availability_status = True

    def __str__(self):
        return f"{self.title} - {self.author} - {self.publicationyear} - {'available' if self.availability_status else 'rented'}"
    
class Patron:
    def __init__(self, name):
        self.name = name
        self.rented_books = []

    def rent_book(self, book):
        if book.availability_status:
            book.mark_as_rented()
            self.rented_books.append(book)
            print(f"{self.name} rented {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self, book):
        if book in self.rented_books:
            book.mark_as_available()
            self.rented_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not rent {book.title}")

    def list_rented_books(self):
        if self.rented_books:
            print(f"{self.name}'s rented books:")
            for book in self.rented_books:
                print(book)
        else:
            print(f"{self.name} has no rented books.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                print(book)
        else:
            print("No books available.")
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

def menu():
    print("Library Rental System Menu")
    print("1. List Available Books")
    print("2. Rent a Book")
    print("3. Return a Book")
    print("4. List Rented Books")
    print("5. Add a Book to Library")
    print("6. Exit")

def main():
    store = Library()
    store.add_book(Book(" to kill a mockingbird ", "harper lee ", 2010))
    store.add_book(Book(" 1984 ", " george orwell ", 1999))
    store.add_book(Book(" the road ", " cormac McCarthy ", 1972))

    patrons = {
        "Alice": Patron("Alice"),
        "Bob": Patron("Bob")
    }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            store.list_books()

        elif choice == "2":
            patron_name = input("Enter your name: ").strip()
            book_title = input("Enter book title to rent: ").strip()
            patron = patrons.get(patron_name)
            book = store.find_book(book_title)
            if patron and book:
                patron.rent_book(book)
            elif not patron:
                print("Patron not found.")
            elif not book:
                print("Book not found.")

        elif choice == "3":
            patron_name = input("Enter your name: ").strip()
            book_title = input("Enter book title to return: ").strip()
            patron = patrons.get(patron_name)
            book = store.find_book(book_title)
            if patron and book:
                patron.return_book(book)
            elif not patron:
                print("Patron not found.")
            elif not book:
                print("Book not found.")

        elif choice == "4":
            patron_name = input("Enter your name: ").strip()
            patron = patrons.get(patron_name)
            if patron:
                patron.list_rented_books()
            else:
                print("Patron not found.")

        elif choice == "5":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            publicationyear = int(input("Enter book year: ").strip())
            store.add_book(Book(title, author, publicationyear))
            print(f"Book '{title}' added to the library")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
