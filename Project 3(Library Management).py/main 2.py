class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAalilableBook(self):

        print('The available books are::')
        for book in self.books:
            print('     ***' + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f'You have been issued the {bookName} book\n , Please keep it safe until it returned')
            self.books.remove(bookName)
            return True
        else:
            print('Sorry!, this book have already been issued!, please select others**')
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for return this book within time ! Have a good day ahead***')


class Student:

    def requestBook(self):
        self.books = input('Enter the name of the book you want to borrow ::')
        return self.books

    def returnBook(self):
        self.books = input(
            'Enter the name of the book you want to return  :: ')
        return self.books


if __name__ == '__main__':

    centralLibrary = Library(['Math', 'Django', 'Algorithm', 'Data Structure'])
    # centralLibrary.displayAalilableBook()

    student = Student()

    while True:
        welcomeMsg = '''**=== Welcome to Central Library ===**

        Please choose an option:

        1. Show the available book list
        2. Request to borrow a book
        3. Return a book
        4. Exit to the library

'''
        print(welcomeMsg)
        try:
            a = int(input('Enter your choice:: '))

            if a == 1:
                centralLibrary.displayAalilableBook()
            elif a == 2:
                centralLibrary.borrowBook(student.requestBook())
            elif a == 3:
                centralLibrary.returnBook(student.returnBook())
            elif a == 4:
                print('Thanks for choosing the centralLibrary')
                exit()
            else:
                print('Invalid choice, Please choose from the option****')
        except Exception as e:

            print(e)


# class Library:

#     def __init__(self, listOfBooks):
#         self.books = listOfBooks

#     def displayAalilableBook(self):
#         print('The books available in this library is :')
#         for books in self.books:
#             print('   **' + books)

#     def borrowBook(self, bookName):
#         if bookName in self.books:
#             print(
#                 f'** Your have been issued this {bookName} book, \nPlease keep it safe and return it within 30 days**')
#             self.books.remove(bookName)
#             # return True
#         else:
#             print(
#                 f'Sorry this {bookName} book have been issued by anyone else, please select a other book')
#             # return False

#     def returnBook(self, bookName):
#         self.books.append(bookName)
#         print(
#             f' ** Thanks for return this {self.books} book within time, Have a good day!!')


# class Student:

#     def requestBook(self):
#         self.books = input(
#             'Please Enter the name of the book you want to borrow:  ')
#         return self.books

#     def returnBook(self):
#         self.books = input(
#             'Please Enter the name of the book you want to return:  ')
#         return self.books


# if __name__ == '__main__':
#     centrallibrary = Library(['Math', 'Basic Electrical',
#                               'Physics', 'Advance Physics'])
#     # centrallibrary.displayAalilableBook()

#     student = Student()

#     while (True):
#         welcomeMsg = ''' Please select form the option
#                         1. Display all the available book in this library
#                         2. Request or borrow a book
#                         3. Return a book
#                         4. Exit to the library

#     '''
#         print(welcomeMsg)

#         try:
#             a = int(input('Enter your choice: '))

#             if a == 1:
#                 centrallibrary.displayAalilableBook()
#             elif a == 2:
#                 centrallibrary.borrowBook(student.requestBook())
#             elif a == 3:
#                 centrallibrary.returnBook(student.returnBook())
#             elif a == 4:
#                 print(
#                     'Thanks for using out CentralLibrary as a refernal... Have a good day!')
#                 exit()

#         except Exception as e:
#             print(f'Please enter a intizer value, error is --> {e}')
