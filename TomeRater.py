# Import regular expressions
import re

# User class definition
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} # Books: ratings

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The user {n}'s email has been updated to {e}".format(n = self.name, e = self.email))
        
    def read_book(self, book, rating = None):
        self.books[book] = rating
        
    def get_average_rating(self):
        average = 0
        total = 0
        length = 0
        for rating in self.books.values():
            if rating is not None:
                total += rating
                length += 1
        if length > 0:
            average = total / length
        return average

    def __repr__(self):
        read = len(self.books)
        return "User: {n}\nEmail address: {e}\nBooks read: {r}".format(n = self.name, e = self.email, r = read)
        
    def __hash__(self):
        return hash((self.name, self.email))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

# Book class definition
class Book:
    def __init__(self, title, isbn, price = 0):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The book {t}'s ISBN has been updated to {i}".format(t = self.title, i = self.isbn))

    def add_rating(self, rating):
        if rating is None:
            pass
        elif rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
            
    def get_average_rating(self):
        average = 0
        total = 0
        for rating in self.ratings:
            total += rating
        if len(self.ratings) > 0:
            average = total / len(self.ratings)
        return average
        
    def add_price(self, new_price):
        self.price = new_price
        print('The price of {t} has been set to ${p}'.format(t = self.title, p = self.price))

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn and self.price == other_book.price
        
    def __hash__(self):
        return hash(self.title) # removed isbn and price hashes to avoid referencing errors when changing isbn or price after already populating TomeRater objects with books. ISBNs are checked in another way for duplicates anyhow.
        
    def __repr__(self):
        return "{t} with ISBN {i}, valued at ${p}".format(t = self.title, i = self.isbn, p = self.price)
        
# Book Subclasses definitions
class Fiction(Book):
    def __init__(self, title, author, isbn, price = 0):
        super().__init__(title, isbn, price)
        self.author = author
        
    def get_author(self):
        return self.author
        
    def __repr__(self):
        return "{t} by {a}, valued at ${p}".format(t = self.title, a = self.author, p = self.price)
            
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price = 0):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
        
    def __repr__(self):
        grammerFix = ''
        if self.level[0] == 'a' or self.level[0] == 'e' or self.level[0] == 'i' or self.level[0] == 'o': # Not totally accurate, but closer.
            grammerFix = 'n'
        return "{t}, a{n} {l} manual on {s}, valued at ${p}".format(t = self.title, n = grammerFix, l = self.level, s = self.subject, p = self.price)
            
# Helper functions                
def get_winner(source, method):
    counts = [method(object) for object in source]
    winnerCount = max(counts)
    winners = [object for object in source if method(object) == winnerCount]
    if len(winners) > 1:
        print("It's a tie!")
    return winners
    
def get_n_most(n, source, count_method, return_method, key_or_value, prompt_object, prompt_descript):
    rotating_objects = dict(source) # Real copy of dictionary to temporarily pop values out of.
    tops = []
    if n > len(rotating_objects):
        n = len(rotating_objects) # Ensures against ValueError
        print('Given requested number of most {descript} {object} exceeded total stored {object} for given instance of TomeRater.\nAll {object} are returned in order of most {descript}.'.format(object = prompt_object, descript = prompt_descript))
    while len(tops) < n:
        if key_or_value == "key":
            counts = [count_method(object) for object in list(rotating_objects)]
            winnerCount = max(counts)
            winners = [object for object in list(rotating_objects) if count_method(object) == winnerCount] # Account for ties
        else:
            counts = [count_method(object) for object in rotating_objects.values()]
            winnerCount = max(counts)
            winners = [value for value, object in rotating_objects.items() if count_method(object) == winnerCount] # Account for ties
        tops += winners
        for winner in winners: # Remove tops to find next tier
            rotating_objects.pop(winner) 
    tops = tops[:n] # Ties are cut off and not returned
    results = [return_method(object) for object in tops]
    return results
            
# Define TomeRater class - Main application
class TomeRater:
    def __init__(self):
        self.users = {} # Emails: User object
        self.books = {} # Book object: Number of Users who have read it
        self.isbns = [] # To track potential duplicates
        
    def create_book(self, title, isbn, price = 0):
        if isbn not in self.isbns:
            self.isbns.append(isbn)
            book = Book(title, isbn, price)
        else:
            raise Exception("The ISBN {i} is already taken.".format(i = isbn))
        return book
        
    def create_novel(self, title, author, isbn, price = 0):
        if isbn not in self.isbns:
            self.isbns.append(isbn)
            book = Fiction(title, author, isbn, price)
        else:
            raise Exception("The ISBN {i} is already taken.".format(i = isbn))
        return book
        
    def create_non_fiction(self, title, subject, level, isbn, price = 0):
        if isbn not in self.isbns:
            self.isbns.append(isbn)
            book = Non_Fiction(title, subject, level, isbn, price)
        else:
            raise Exception("The ISBN {i} is already taken.".format(i = isbn))
        return book
        
    # Set new ISBNs from here to insure no duplicates are made from changing the book objects directly by referencing to the TomeRater object's ISBN list:
    def set_isbn(self, book, new_isbn):
        if new_isbn not in self.isbns:
            self.isbns[self.isbns.index(book.isbn)] = new_isbn
            book.set_isbn(new_isbn)
        else:
            print("The ISBN {i} is already taken".format(i = new_isbn))        
        
    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email)
        if user is None:
            print("No user with email: {e}!".format(e = email))
        else:
            user.read_book(book, rating)
            book.add_rating(rating)
            if self.books.get(book) == None:
                self.books[book] = 1
            else:
                self.books[book] += 1
    
    def add_user(self, name, email, user_books = None):
        com_search = re.search(r'\.com', email)
        edu_search = re.search(r'\.edu', email)
        org_search = re.search(r'\.org', email)
        
        if email.count('@') == 1:
            if (    email[-4:] == '.com' and edu_search is None and org_search is None
                 or email[-4:] == '.edu' and com_search is None and org_search is None
                 or email[-4:] == '.org' and com_search is None and edu_search is None
               ):
                user = User(name, email)
                if self.users.get(email) is None:
                    self.users[email] = user
                    if user_books is not None:
                        for book in user_books:
                            self.add_book_to_user(book, email)
                elif self.users.get(email) == user:
                    print("The user {n} already exists!".format(n = user.name))
                else:
                    print("The email address {e} is already associated with another user!".format(e = email))
            else:
                print("The entered email address must end in either '.com' '.edu' or '.org'")
        else:
            print("The entered email address must include a single '@' sign.")
            
    def print_catalog(self):
        for book in list(self.books):
            print(book)
            
    def print_users(self):
        for user in self.users.values():
            print(user)
            
    def most_read_book(self):
        def method(object):
            return self.books[object]    
        winners = get_winner(list(self.books), method)
        return winners     
                
    def highest_rated_book(self):
        def method(object):
            return object.get_average_rating()
        winners = get_winner(list(self.books), method)
        return winners
        
    def most_positive_user(self):
        def method(object):
            return object.get_average_rating()
        winners = get_winner(self.users.values(), method)
        return winners
    
    def get_n_most_read_books(self, n):
        def count_method(object):
            return self.books[object]
        def return_method(object):
            return object.title
        results = get_n_most(n, self.books, count_method, return_method, "key", "books", "read")
        return results
    
    def get_n_most_prolific_readers(self, n):
        def count_method(object):
            return len(object.books)
        def return_method(object):
            return self.users[object].name
        results = get_n_most(n, self.users, count_method, return_method, "value", "users", "prolific")
        return results    

    def get_n_most_expensive_books(self, n):
        def count_method(object):
            return object.price
        def return_method(object):
            return object.title
        results = get_n_most(n, self.books, count_method, return_method, "key", "books", "expensive")
        return results            

    def get_worth_of_user(self, user_email):return sum(prices)

    # My own idea of improving TomeRater:
    def get_book_by_isbn(self, isbn):
        if isbn not in self.isbns:
            raise Exception("The ISBN {i} was not found in this instance.".format(i = isbn))
        else:
            title = [book.title for book in self.books if book.isbn == isbn]
            return title[0] # Should anyway only be a list of length 1    

    def __repr__(self):
        n_users = len(self.users)
        s_users = ''
        if n_users > 1 or n_users == 0:
            s_users = 's'
        n_books = len(self.books)
        s_books = ''
        if n_books > 1 or n_books == 0:
            s_books = 's'
        return "A book rating application currently storing {n_users} user{s_users} with their ratings of {n_books} book{s_books}.".format(n_users = n_users, s_users = s_users, n_books = n_books, s_books = s_books)
        
    def __eq__(self, other_rater):
        return self.users == other_rater.users and self.books == other_rater.books and self.isbns == other_rater.isbns
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
