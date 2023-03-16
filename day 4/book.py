class Book:
    def __init__(self):
        self.title = None

my_fav = Book()
my_fav.title = "Head first programming"
your_fav = Book()
your_fav.title = "Learn python the hard way"

my_fav.title = "Learning python"

print(my_fav.title)
print(your_fav.title)