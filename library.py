def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    with open("books.txt", "a") as f:
        f.write(title + "," + author + "\n")
    print("Book added successfully!")
def search_book():
    key = input("Enter title or author to search: ").lower()
    with open("books.txt", "r") as f:
        found = False
        for book in f:
            if key in book.lower():
                print(book.strip())
                found = True
        if not found:
            print("Book not found")
def report():
    with open("books.txt", "r") as f:
        books = f.readlines()
    print("Total books:", len(books))
    author = input("Enter author name: ").lower()
    for book in books:
        details = book.strip().split(",")
        if details[1].lower() == author:
            print(book.strip())
open("books.txt", "a").close()
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Report")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        report()
    elif choice == "4":
        break
    else:
        print("Invalid choice")