class Movieclass:
    def __init__(self,title,genre,year):
        self.title=title
        self.genre=genre
        self.year=year
        self.available=True

    def mark_as_rented(self):
        self.available=False
        
    def mark_as_available(self):
        self.available=True

    def __str__(self):
        return   f"{self.title}{self.genre}{self.year} {'available' if self.available else'rented'}

class Customer:
    def  __init__(self, name):
        self.name=name
        self.rented_movies= []

    def rent_movie(self, movie):
        if  movie.available:
            movies.mark_as_rented()
            self.rented_movies.append(movie)
            print(f"{self.name} rented {movie.title}")
        else:
              print(f"{movie.title} is not available")
    
    
    def  return_movies(self,movie):
        if movie in self.rented_movie:
            movie.mark_as_available()
            self.rented_movies.remove(movie)
            print(f"{self.name} returned {movie.title}")
        else:
            print(f"{self.name} did not rent {movie.title}")

    def List_rented_movies(self):
        if self.rented_movies:
            print(f"{self.name} 's rented movies:")
            for movie in self.rented_movies:
                print(movie)
        else:
            print(f"{self.name} has no rented movies. ")

class Rentalstore:
    def __init__(self):
        self.movies=[]

    def add_movies(self,movie):
        self.movies.append(movie)
         
    def list_movies(self):
        if self.movies:
            print("available movies:")
            for movie in self.movies:
                print(movie)
        else:
            print("no movies available. ")

    def find_movies(self,title):
        for movie in self.movies:
            if movie.title.lower()==title.lower():
                return movie
            return None
    def menu():
        print("/nmovie rental system menu")
        print("1. list available movies")
        print("3. returnm a movie")
        print("4. list rented movies")
        print("5. add a movie to store")
        print("6. exit")

def main():
        store=Rentalstore()
        store.add_movies(movie("inception","sci-fi",2010))
        store.add_movies(movie("the matrix","action",1999))
        store.add_movies(movie("the god father", "crime",1972))

    customers={
    "alice":customer("alice")
    "bob":Customer("bob")
    }

    while True:
        menu()
        choice = input("enter your choice: ").strip()

        if choice == "1":
            store.list_movies()
        elif choice =="2":
            