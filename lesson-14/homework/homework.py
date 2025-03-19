import json

def load_books():
    try:
        with open('books.json') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
def save_books(books):
    with open('books.json','w') as file:
        json.dump(books,file,indent=4)

def add_book():
    books=load_books
    title=input("Enter title of the book:")
    author=input("Enter author:")
    year=input("Enter publication year:")

    books.append({"title":title, "author":author, "year":year})
    save_books(books)
    print("The book successfully added!\n")

def update_book():
    books=load_books()
    title=input("Enter the title of the book to update: ")
    for book in books:
        if book ["title"].lower ()==title.lower():
            book["author"]=input("Enter new author:")
            book["year"]=input("Enter new year:")
            save_books()
            print("Updated successfully!")
            return
    print('Book not found')

def delete_book():
    books=load_books()
    title=input("Enter the name of book to delete:")
    books=[book for book in books if book["title"].lower() !=title.lower()]
    save_books()
    print('Deleted successfully!')

def display_book():
    books=load_books()
    if not books:
        print('The book not found!')
        return
    for idx, bood in enumerate(books, start=1):
        print(f'{idx}.{book['title']} by {book['author']} ({book['year']})')
        print() 

def main():
    while True:
        print("\nBook maganer")
        print('1. Add book')
        print('2. Update book')
        print('3. Delete book')
        print('4. Display book')
        print('5. Exit')
        choise=input("Enter your choise")

        if choise ==1:
            add_book()
        if choise ==2:
            update_book()
        if choise ==3:
            delete_book()
        if choise ==4:
            display_book()
        if choise==5:
            print("Goodbye!")
            break
        else:
            print('Invalid choise')
if __name__=="__name__":
    main()