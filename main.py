from book import Book

b1 = Book(1122, "Learn Python", "pasep")
b2 = Book(1001, "Unit Test", "skyla")

print(b1.get_title())
print(b2.get_title())

b1.set_title("Belajar Python")

print(b1.get_title())
print(b2.get_title())
