FileName = r"C:\Users\rohan\OneDrive\Desktop\New folder (2)\Library system.txt"

def add_book(library):
    file = open(FileName, "a")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    status = "Available"

    book = {'Title': title, 'Author': author, 'Available': status}
    library.append(book)
    file.write(title + " by " + author + " - " + status + "\n")
    file.close()

    print("Book '" + title + "' added successfully!")

def view_books(FileName):
    file = open(FileName, "r")
    books = file.readlines()
    file.close()

    if not books:
        print("No books in the library yet.")
        return

    print("\nLibrary Collection:")
    for i, book in enumerate(books, 1):
        print(str(i) + ". " + book.strip())

def search_books(FileName):
    query = input("Enter the book title or author to search: ").lower()
    file = open(FileName, "r")
    books = file.readlines()
    file.close()

    found = False
    print("\nSearch Results:")
    for book in books:
        if query in book.lower():
            print(book.strip())
            found = True

    if not found:
        print("No matching books found.")

def mark_unavailable(FileName):
    book_name = input("Enter the book name to mark as unavailable: ").lower()

    file = open(FileName, "r")
    books = file.readlines()
    file.close()

    updated_books = []
    for book in books:
        book = book.strip()
        if book_name in book.lower():
            if "Available" in book:
                book = book.replace("Available", "Unavailable")
                print("The book '" + book_name + "' has been marked as unavailable.")
            else:
                print("The book '" + book_name + "' is already unavailable.")
        updated_books.append(book + "\n")

    file = open(FileName, "w")
    file.writelines(updated_books)
    file.close()

def mark_available(FileName):
    book_name = input("Enter the book name to mark as available: ").lower()

    file = open(FileName, "r")
    books = file.readlines()
    file.close()

    updated_books = []
    for book in books:
        book = book.strip()
        if book_name in book.lower():
            if "Unavailable" in book:
                book = book.replace("Unavailable", "Available")
                print("The book '" + book_name + "' has been marked as available.")
            else:
                print("The book '" + book_name + "' is already available.")
        updated_books.append(book + "\n")

    file = open(FileName, "w")
    file.writelines(updated_books)
    file.close()

def library_management():
    library = []
    while True:
        print("\nLibrary Management Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Mark Book as Unavailable")
        print("5. Mark Book as Available")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_books(FileName)
        elif choice == '3':
            search_books(FileName)
        elif choice == '4':
            mark_unavailable(FileName)
        elif choice == '5':
            mark_available(FileName)
        elif choice == '6':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

library_management()
