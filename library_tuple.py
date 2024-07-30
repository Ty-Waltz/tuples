library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(title, author):
    new_book = (title, author)
    
    if new_book in library:
        print(f"The book '{title}' by {author} already exists.")
    else:
        library.append(new_book)
        print(f"The book '{title}' by {author} has been added to the library.")

def show_library():
    print("Library:")
    for index, (title, author) in enumerate(library):
        print(f"{index + 1}. '{title}' by {author}")


def menu():
    print("1. Add a new book")
    print("2. Show library")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        add_book(title, author)
    elif choice == "2":
        show_library()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("That is not a valid option. Please try again.")