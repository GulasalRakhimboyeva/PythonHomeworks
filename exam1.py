# PYTHON TASKS (Easy → Hard) 
 
# EASY (10 ball) 
# Task: 
# Berilgan butun son n. 
# Agar son: 
# - juft bo‘lsa "Even" 
# - toq bo‘lsa "Odd" 
# - agar son 0 bo‘lsa "Zero" chiqarsin. 

 
# Misol: 
# Input: 8 
# Output: Even 
 
# Input: 0 
# Output: Zero 

# solution
number=int(input('Input: '))

if number==0:
    print('Output: Zero')
elif number%2==0:
    print('Output: Even')
else:
    print('Output: Odd')
 
 
# MEDIUM (15 ball) 
# Task: 
# Foydalanuvchidan matn (string) kiritishni so‘raydigan va so‘ngra shu matnning teskari (reverse) ko‘rinishini chiqaradigan Python dasturini yozing.

# Masalan, agar foydalanuvchi "Hello, World!" deb kiritsa, dastur  "!dlroW ,olleH" natijasini chiqarishi kerak.
 
# solution
text=input("Enter your text: ")
print(text[::-1])
 
# MEDIUM (15 ball) 
# Task: 
# Berilgan songacha tub (prime) sonlarni hosil qiladigan Python dasturini yozing.


# Dasturingiz quyidagilarni bajarishi kerak:

# Foydalanuvchidan yuqori chegara sifatida musbat butun son kiritishni so‘rang.

# Kiritilgan chegaragacha bo‘lgan barcha tub sonlarni topish algoritmini amalga oshiring.

# Topilgan tub sonlar ro‘yxatini ekranga chiqaring.

# Masalan, agar foydalanuvchi chegara sifatida 20 ni kiritsa, dastur 20 ga teng yoki undan kichik tub sonlarni chiqarishi kerak:
# [2, 3, 5, 7, 11, 13, 17, 19].

# solution
prime_list=[]
n=int('Enter number: ')
for i in range(2, n+1):
    for k in range(2, i):
        if i%k!=0:
            prime_list.append(i)  #not completed
 
 
# MEDIUM+ (20 ball) 
# Task: 
# Berilgan sonlar ro‘yxati nums. 
# Har bir element nechta marta uchrashganini hisoblab, natijani dict ko‘rinishida chiqaring. 
 
# Misol: 
# Input: [1,2,2,3,3,3] 
# Output: 
# {1:1, 2:2, 3:3} 
#solution
nums=[1,2,2,3,3,4] 
output={}
for i in nums:
    output[i]=str(nums).count(str(i))
print(output)

# HARD (25 ball) 
# Task: 
# Shart: Book va Library classlarini yarating.

# Book class: title, author, va is_borrowed (default False) xususiyatlariga ega bo'lsin.

# Library class:

# books ro'yxati (bu yerda Book obyektlari saqlanadi).

# add_book(book) – yangi kitob qo'shish.

# borrow_book(title) – kitobni ijaraga berish. Agar kitob kutubxonada bo'lsa va ijaraga olinmagan bo'lsa, is_borrowed ni True ga o'zgartirsin. Aks holda "Kitob band" yoki "Mavjud emas" desin.

# return_book(title) – kitobni qaytarish.

# # search_by_author(author) – berilgan muallifning barcha kitoblarini qaytarsin.

#solution
class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed

class Library(list):
    def add_book(self, book: Book):
        self.book=book
        self.append(self.book)
    def borrow_book(self, title, book: Book):
        self.title=title
        if book.title in self:

            if not book.is_borrowed:
                book.is_borrowed=True
            else:
                return 'Kitob band'
        else:
            return 'Mavjud emas'
    def return_book(self, title, book: Book):
        self.title=title
        book.is_borrowed=False
    
    def search_by_author(self, author):
        for book in self:
            if book.author==author:
                return book

