class Book:
    total_books = 0  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Automatically increment when a book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Usage
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    print("Total books:", Book.total_books)
