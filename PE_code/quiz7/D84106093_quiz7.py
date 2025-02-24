library = {}

def add_book():


    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here
    ui = input("Enter the title, genre, and price of the book (seperated by |): ") #get the user input
    ui_list = ui.split("|") #split the input, get the title, genre, price separately
    library[ui_list[0]] = (ui_list[1],int(ui_list[2])) #update with new books
    print("\nAdded %s to the library."%ui_list[0])

    return True

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.

    """
    
    # your code here

    ui = input("Enter the title of the book to remove: ")

    value = library.pop(ui, None) #if there is no corresponding title, then we use the default value None for representation
    if value is None:
        print("\nError: %s not found in the library.\n"%ui)
        return False
    else:
        print("\nRemoved %s from the library\n"%ui)
        return True


def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    ui = input("Enter the title of the book: ")

    if ui in library:
        g, p = library[ui]#genre and price 
        print("\nTitle: %s \nGenre: %s\nPrice: %d \n"%(ui,g,p))
    else:
        print("\nError: %s not found in the library.\n"%ui)
        

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """

    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here
    ui = input("Enter the genre to search for: ")
    find = 0 #record the numbers of matched genre
    for title, (genre, price) in sorted(library.items()): #sort the dict library with the slphabetical order
        if genre ==ui:
            print("%s (%s, $%.2f)"%(title,genre,price))
            find+=1
    print()
    if find ==0:
        print("\nNo book found in the %s genre.\n"%ui)
        return False
    else:
        return True

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

