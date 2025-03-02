class Book:
    def __init__(self, title, author, year):
        self.title = title  
        self.author = author  
        self.year = year  

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = [
            Book("python basic", "games gosling", "1960"),
            Book("core java", "George Orwell", "1949"),
            Book("C complete course", "Jane Austen", "1813"),
            Book("AWS", "F. Scott Fitzgerald", "1925"),
            Book("Advance python", "Aldous Huxley", "1932")
        ] 

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the publication year of the book: ")
        
        new_book = Book(title, author, year)
        
        self.books.append(new_book)
        print(f"The book '{title}' has been added to the library.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        
        new_books = []
        
        # Loop through all the books in the library
        for book in self.books:
            if book.title != title:  
                new_books.append(book)
        
        # Update the library's book list with the new list 
        self.books = new_books
        print(f"The book '{title}' has been removed from the library.")

    def search_book(self):
        title = input("Enter the title (or part of the title) to search for: ")
        
        # Create a list to store books that match the search
        found_books = []
        
        for book in self.books:
            if title.lower() in book.title.lower():  
                found_books.append(book)
        
        # If we found matching books
        if found_books:
            print("Found books:")
            for book in found_books:
                print(book)
        else:
            print("No books found with that title.")

    def display_books(self):
        if self.books:                        
            for book in self.books:
                print(book)
        else:
            print("There are no books in the library.")


def main():
    library = Library()

    while True:
        print("\nChoose an option:")
        print("1: Add a Book")
        print("2: Remove a Book")
        print("3: Search for a Book")
        print("4: Display all Books")
        print("5: Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.add_book() 
        elif choice == "2":
            library.remove_book()  
        elif choice == "3":
            library.search_book()  
        elif choice == "4":
            library.display_books()  
        elif choice == "5":
            print("Exiting the program") 
            break  
        else:
            print("Invalid choice. Please choose a number between 1 and 5.") 

run = main  
run()
