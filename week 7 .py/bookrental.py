class Book:
    def __init__(self,title,author,publicationyear):
        self.title=title
        self.author=author
        self.publicationyear=publicationyear
        self.availability_status=True
    
    def mark_as_rented(self):
        self.availability_status=False

    def mark_as_available(self):
        self.availability_status=True

    def __str__(self):
        return f"{self.title} - {self.author} - {self.publicationyear} - {'available' if self.availability_status else 'rented'}"
    
class Patron:
    def __init__(self,name):
        self.name=name
        self.available_book=[]

    def rent_book(self,book):
        if book.availability_status:
            book.mark_as_rented()
            self.available_book.append(book)
            print(f"{self.name} rented {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self,book):
        if book in self.available_book:
            book.mark_as_available()
            self.available_book.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} is not available to rent {book.title}")
    def list_rented_books(self):
        if self.available_book:
            print(f"{self.name}'s is rented books")
            for  book in self.available_book:
                print(book)
        else:
            print(f"{self.name} has no rented books.")

class Library:
    def __init__(self):
        self.book=[]

    def add_book(self, book):
        self.book.append(book)

    def list_book(self):
        if self.book:
            print("Available book:")
            for book in self.book:
                print(book)
        else:
            print("No book available.")
    
    
    def find_movie(self, title):
        for book in self.book:
            if book.title.lower() == title.lower():
                return book
        return None
   
def menu():
        print("books Rental System Menu")
        print("1. List Available books")
        print("2. Rent a books")
        print("3. Return a books")
        print("4. List Rented books")
        print("5. Add a books to Store")
        print("6. Exit")

        #copy
def main():
    store = Library()
    store.add_book(Book("Inception", "Sci-Fi", 2010))
    store.add_book(Book("The Matrix", "Action", 1999))
    store.add_book(Book("The Godfather", "Crime", 1972))

    patrons = {
        "Alice": Patron("Alice"),
        "Bob": Patron("Bob")
     }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.list_books()

        elif choice == "2":
            customer_name = input("Enter your name: ").strip()
            book_title = input("Enter book title to rent: ").strip()
            library = library.get(customer_name)
            book = store.find_book(book_title)
            if library and book:
                library.rent_book(book)
            elif not library:
                print("library not found.")
            elif not book:
                print("book not found.")

        elif choice == "3":
            customer_name = input("Enter your name: ").strip()
            book_title = input("Enter book title to return: ").strip()
            library = library.get(customer_name)
            book = store.find_book(book_title)
            if library and book:
                library.return_book(book)
            elif not library:
                print("Customer not found.")
            elif not book:
                print("book not found.")

        elif choice == "4":
            customer_name = input("Enter your name: ").strip()
            library = library.get(customer_name)
            if library:
                library.list_rented_movies()
            else:
                print("Customer not found.")

        elif choice == "5":
            title = input("Enter book title: ").strip()
            author = input("Enter book genre: ").strip()
            publicationyear = int(input("Enter book year: ").strip())
            store.add_book(book(title, author, publicationyear))
            print(f"books '{title}' added to the store")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if  __name__ == "__main__":
    main()
