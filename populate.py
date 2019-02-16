from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
# Test for duplicate ISBN
#book1_test = Tome_Rater.create_book("Society of Mind 2", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
#novel1.set_isbn(9781536831139) # Commented out to try with new TomeRater.set_isbn() method
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 2)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 20)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
# Test for duplicate user:
#Tome_Rater.add_user("David Marr", "david@computation.org")
# Test for duplicate emails:
#Tome_Rater.add_user("Burt Bob", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)
# Tie maker for most read:
Tome_Rater.add_book_to_user(novel1, "david@computation.org", 3) 

# New set_isbn method that tracks ISBN duplicates:
#Tome_Rater.set_isbn(novel1, 9781536831139)
#Tome_Rater.set_isbn(novel2, 9781536831139)

# Add users with an invalid email:
#Tome_Rater.add_user("Burt Bob", "burters.com")
#Tome_Rater.add_user("Burt Bob", "burters@bob.coms")
#Tome_Rater.add_user("Burt Bob", "burters@bob.org.com")
#Tome_Rater.add_user("Burt Bob", "burt@ers@bob.com")

# Test TomeRater Object print:
#print(Tome_Rater)

# Test two equal TomeRater Objects:
#Tome_Rater2 = TomeRater()
#Tome_Rater2.add_user("Bernie", "berns@stuff.com")
#Tome_Rater2.add_book_to_user(novel1, "berns@stuff.com")
#print(Tome_Rater == Tome_Rater2)
#Tome_Rater3 = TomeRater()
#Tome_Rater3.add_user("Bernie", "berns@stuff.com")
#Tome_Rater3.add_book_to_user(novel1, "berns@stuff.com")
#print(Tome_Rater2 == Tome_Rater3)

# Test Most Read Books:
#print(Tome_Rater.get_n_most_read_books(9))

# Test Most Prolific Readers:
#print(Tome_Rater.get_n_most_prolific_readers(2))

# Test Price variable:
#novel1.add_price(5)

# Test Most Expensive Books:
#print(Tome_Rater.get_n_most_expensive_books(4))

# Test User worth:
#print('$',Tome_Rater.get_worth_of_user("alan@turing.com"))
#print('$',Tome_Rater.get_worth_of_user("al@g.com")) # Should catch the invalid email

# Test my function of Get Book by ISBN:
print(Tome_Rater.get_book_by_isbn(10001000)) # Soft Rains
#print(Tome_Rater.get_book_by_isbn(1903847109)) # Invalid

#Uncomment these to test your functions:
#Tome_Rater.print_catalog()
#Tome_Rater.print_users()

#print("Most positive user:")
#print(Tome_Rater.most_positive_user())
#print("Highest rated book:")
#print(Tome_Rater.highest_rated_book())
#print("Most read book:")
#print(Tome_Rater.most_read_book())
