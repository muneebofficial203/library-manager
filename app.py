import json  # Importing JSON module to handle data storage

# File to store library data
LIBRARY_FILE = "library.json"

def load_library():
    """Load library data from file."""
    try:
        with open(LIBRARY_FILE, "r") as file:  # Open the library file in read mode
            return json.load(file)  # Load JSON data from file
    except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or corrupt JSON
        return []  # Return an empty list if the file does not exist or has errors

def save_library(library):
    """Save library data to file."""
    with open(LIBRARY_FILE, "w") as file:  # Open the library file in write mode
        json.dump(library, file, indent=4)  # Save the library data with indentation for readability

def add_book(library):
    """Add a new book."""
    book = {
        "title": input("Enter book title: ").strip(),  # Get book title from user
        "author": input("Enter author: ").strip(),  # Get author name
        "year": int(input("Enter publication year: ").strip()),  # Get and convert year to integer
        "genre": input("Enter genre: ").strip(),  # Get book genre
        "read": input("Have you read this book? (yes/no): ").strip().lower() == "yes"  # Convert input to boolean
    }
    library.append(book)  # Add book to the library list
    save_library(library)  # Save updated library
    print("Book added!\n")

def remove_book(library):
    """Remove a book by title."""
    title = input("Enter book title to remove: ").strip()  # Get book title to remove
    library[:] = [book for book in library if book["title"].lower() != title.lower()]  # Remove book if title matches
    save_library(library)  # Save updated library
    print("Book removed!\n")

def search_books(library):
    """Search books by title or author."""
    query = input("Enter title or author: ").strip().lower()  # Get search query
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]  # Find matching books
    print("\nResults:")
    for book in results:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {'Read' if book['read'] else 'Unread'}")  # Display book details
    if not results:
        print("No matches found.")  # Print message if no matches
    print()

def display_books(library):
    """Display all books."""
    print("\nLibrary Collection:")
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {'Read' if book['read'] else 'Unread'}")  # Print all books
    if not library:
        print("No books available.")  # Show message if no books exist
    print()

def display_statistics(library):
    """Show library statistics."""
    total = len(library)  # Get total number of books
    read = sum(1 for book in library if book['read'])  # Count books marked as read
    print(f"\nTotal Books: {total}, Read: {read} ({(read / total * 100) if total else 0:.2f}%)\n")  # Display stats with percentage

def main():
    """Run the library manager."""
    library = load_library()  # Load library data from file
    actions = {
        "1": add_book, "2": remove_book, "3": search_books, "4": display_books, "5": display_statistics  # Map menu options to functions
    }
    while True:
        print("1. Add  2. Remove  3. Search  4. Show  5. Stats  6. Exit")  # Display menu
        choice = input("Choose an option: ").strip()  # Get user choice
        if choice == "6":
            print("Goodbye!")  # Exit the program
            break
        actions.get(choice, lambda x: print("Invalid choice.\n"))(library)  # Execute selected function or show error

if __name__ == "__main__":
    main()  # Start the program