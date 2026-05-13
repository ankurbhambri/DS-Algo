'''
Designing an online book reader (like Kindle or Google Books) requires balancing a massive library of content with the personal experience of an individual reader.
'''

class Page:
    def __init__(self, page_num, text):
        self.page_num = page_num
        self.text = text


class Book:
    def __init__(self, book_id, title, author, pages):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.pages = pages


class UserProgress:
    def __init__(self, book_id):
        self.book_id = book_id
        self.current_page = 0  # Starts at the beginning


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.library = {}  # Stores {book_id: UserProgress}


class OnlineReaderSystem:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.active_user = None

    def add_user(self, user_id, name):
        self.users[user_id] = User(user_id, name)

    def add_book(self, book_id, title, author, pages):
        self.books[book_id] = Book(book_id, title, author, pages)

    def set_active_book(self, book_id, user_id=None):

        if user_id is None:
            print("Error: No user specified!")
            return

        self.active_user = self.users.get(user_id, None)
        if self.active_user is None:
            print("Error: No user found!")
            return

        # If the user doesn't have this book in their personal library, add it
        if book_id not in self.active_user.library:
            self.active_user.library[book_id] = UserProgress(book_id)

        # Get the progress and fetch the page
        progress = self.active_user.library[book_id]
        book = self.books[book_id]
        page = book.pages[progress.current_page]

        print(f"--- {self.active_user.name} is now reading {book.title} ---")
        print(f"Page {page.page_num}: {page.text}")


reader_system = OnlineReaderSystem()
reader_system.add_user("user1", "Alice")
reader_system.add_book("book1", "The Great Gatsby", "F. Scott Fitzgerald", [
    Page(0, "In my younger and more vulnerable years..."), 
    Page(1, "Gatsby turned out all right at the end...")
])
reader_system.set_active_book("book1", "user1")