'''
Rebeca Llontop 
IS 303 - A05

Task Manager
This program creates a task list where the user can mark as complete 
or incomplete and separates the tasks by priority level. 

Inputs:
- Task name
- Task category
- Priority level (low, medium, high)

Processes:
- Task: stores a tasks's name, category, and priority level, and completion status
- TaskList: stores tasks in a list, can count incomplete tasks, filter tasks by priority
and can display the full tasks list. 

Outputs: 
- Displayed task list by category along with their incomplete/complete mark and 
priority level. 
'''

class Task:
    def __init__(self, name, category, level):
        self.name = name
        self.category = category
        self.level = level
        self.completion = False  

    def mark_complete(self):
        """Marks the task as completed"""
        self.completion = True 

    def __str__(self):
        if self.completion == True:
            return f"{self.name} (Category: {self.category}, Priority: {self.level}) - ✓"
        else:
            return f"{self.name} (Category: {self.category}, Priority: {self.level}) - ✗"


class TaskList:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_book(self, book):
        """Add a Book object to the shelf."""
        self.books.append(book)

    def get_average_pages(self):
        """Return the average page count across all books."""
        if len(self.books) == 0:
            return 0
        total = sum(book.pages for book in self.books)
        return total / len(self.books)

    def get_longest(self):
        """Return the Book with the most pages."""
        if len(self.books) == 0:
            return None
        longest = self.books[0]
        for book in self.books:
            if book.pages > longest.pages:
                longest = book
        return longest

    def __str__(self):
        header = f"Bookshelf: {self.name} ({len(self.books)} books)"
        book_list = ""
        for book in self.books:
            book_list = book_list + f"\n  - {book}"
        return header + book_list


# --- Main Flow ---

shelf = Bookshelf("My Favorites")

shelf.add_book(Book("The Hobbit", "J.R.R. Tolkien", 310))
shelf.add_book(Book("Ender's Game", "Orson Scott Card", 324))
shelf.add_book(Book("The Giver", "Lois Lowry", 208))

print(shelf)
print(f"\nAverage pages: {shelf.get_average_pages():.0f}")

longest = shelf.get_longest()
print(f"Longest book: {longest.title} ({longest.pages} pages)")