class Library:

    def allBooks(a):
        with open('books.txt')as f: 
            t = f.read()
            print(t)

    def borrowedBook(wBook):
        with open('books.txt')as f: 
            t = f.read()
        if wBook in t:
            print(f'The book is available please collect it from libarary and keep it safe and retrun it in 7 Days')
        else:
            print('Sorry, The book is currently not available')

    def retrunBook(bookName):
        print(f'Thanks for Retruning Book Hope you Enjoyed it.\n {bookName} Book Received')        


if __name__== "__main__":
    while (True):
        print('''\n\tPress 1 - List of Books
        Press 2 - Borrowed Book
        Press 3 - Retrun Book
        **************************''')

        user = int(input(''))
        std = Library()
        try:
            if user == 1:
                std.allBooks()

            elif user == 2:
                b=input('Enter a book name you want:\n')
                std.borrowedBook(b)

            elif user == 3:
                r=input('Enter a book name you Want to retrun:\n')
                std.retrunBook(r)

            else:
                print('Invalid Option')

        except Exception as e:
            print(e)
    