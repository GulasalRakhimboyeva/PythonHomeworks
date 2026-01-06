# # ### Number Data Type Questions:
########################################################################
# # 1. Create a program that takes a float number as input and rounds it to 2 decimal places.
# #method1
# float_number=float(input("your number:"))
# print(f"{float_number:.2F}")
# #method2
# float_number=float(input("your number:"))
# print(round(float_number, 2 ))
# #method3
# float_number=float(input("your number:"))
# x=round(float_number, 2)
# print(x)

# # 2. Write a Python file that asks for three numbers and outputs the largest and smallest.
# a=input("first_number:")
# b=input("second_number:")
# c=input("third_number:")
# x=max(a, b, c)
# y=min(a, b, c)
# print(f"max_number:{x} \nmin_number:{y}")

# # 3. Create a program that converts kilometers to meters and centimeters.
# a=int(input("distance in km: "))
# b=a*1000
# c=b*100
# print(f"distance in m: {b} \ndistance in cm:{c}")

# # 4. Write a program that takes two numbers and prints out the result of integer division and theremainder.
# a=int(input("first_number:"))
# b=int(input("second_number:"))
# c=a//b
# d=a%b
# print(f"int_division:{c}\nremainder:{d}")

# # 5. Make a program that converts a given Celsius temperature to Fahrenheit.
# c=float(input("celsius_degree:"))
# f=round(9/5*c+32, 2)
# print(f"fahrenheit_degree:{f}")
# print(c)

# # 6. Create a program that accepts a number and returns the last digit of that number.
# a=str(input("number:"))
# print(f"last_digit:{a[-1]}")

# # 7. Create a program that takes a number and checks if it’s even or not.
# a=int(input("number:"))
# if a%2==0:
#     print("it is even number")
# else:
#     print("it is not even number")
################################################################
### String Questions:
################################################################

# # 1. Create a program to ask name and year of birth from user and tell them their age.
# a=input("What is your name:")
# b=input('When did you born:')
# c=2026-int(b)
# print(f"{a}, you are {c} years old")

# # 2. Extract car names from this text:
# txt = 'LMaasleitbtui'
# print(txt[0::2])
# print(txt[1::2])

# # 3. Write a Python program to:
# #    - Take a string input from the user.
# #    - Print the length of the string.
# #    - Convert the string to uppercase and lowercase.
# a=str(input())
# print(len(a))
# print(a.lower())
# print(a.upper())

# # 4. Write a Python program to check if a given string is `palindrome` or not.
# # > What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
# a=str(input())
# b=a[::-1]
# print(a)
# print(b)
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")

# # 5. Write a program that counts the number of vowels and consonants in a given string.
# a=str(input("something:"))
# vowels="aeouiAOUEI"
# vowel_count=0
# consonant_count=0

# for letter in a:
#     if letter.isalpha():
#         if letter in vowels:
#             vowel_count +=1
#         else:
#             consonant_count +=1

# print("Number of vowels", vowel_count)
# print("Numberof consonants", consonant_count)  
  
# # 6. Write a Python program to check if one string contains another.
# a=input("first:")
# b=input("second:")

# if b in a:
#     print("your second word is in first")
# else:
#     print("your second word is not in first")

# # 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# # Example:  
# #    - Input sentence: "I love apples."  
# #    - Replace: "apples"  
# #    - With: "oranges"  
# #    - Output: "I love oranges."
# sentence=input("Write your sentence:")
# replaces=input("Which word need to be replaced? ")
# withs=input("for what? ")
# print(sentence.replace(replaces, withs))

# # 8. Write a program that asks the user for a string and prints the first and last characters of the string.  
# a=input()
# print(a[0], a[-1])

# # 9. Ask the user for a string and print the reversed version of it.
# a=input()
# print(a[::-1])

# # 10. Write a program that asks the user for a sentence and prints the number of words in it.  
# a=input("write sentence: ")
# b=a.split()
# c=len(b)
# print("you used", c, "words in your sentence")

# # 11. Write a program to check if a string contains any digits.  
# a=input()
# digits=0
# for letter in a:
#     if letter.isdigit():
#       digits +=1
# if digits>0:
#    print("digit exists")    
# else:
#    print("digit does not exist") 

# # 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  
# words = input("Enter words separated by spaces: ").split()
# separator = input("Enter a separator character: ")

# result = separator.join(words)
# print("Joined string:", result)

# # 13. Ask the user for a string and remove all spaces from it.  
# a= input("Enter words separated by spaces: ")
# b=a.replace(" ", "")
# print(b)

# # 14. Write a program to ask for two strings and check if they are equal or not.  
# a=input("first:")
# b=input("second:")

# if b == a:
#     print("your second word is equal to first")
# else:
#     print("your second word is not equal to first")

# # 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
# #     Example:  
# #     - Input: "World Health Organization"  
# #     - Output: "WHO"  
# a=input("your sentence:")
# b=a.split()
# output=""
# for char in b:
#     output += char[0]
# print(output)

# # 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
# a=input("something:")
# b=input("character:")
# d=a.replace(b, "")
# print(d)
# # 17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
# a=input("something:")
# b=input("character:")
# vowel="aeiuoAEIUO"
# d=""
# for char in a:
#     if char in vowel:
#         d+=b
#     else:
#         d+=char

# print(d)

# # 18. Write a program that checks if a string starts with one word and ends with another.  
# #     Example:  
# #     - Input: "Python is fun!"  
# #     - Starts with: "Python"  
# #     - Ends with: "fun!"  
# a=input("sentence:")
# b=input("should begin:")
# c=input("should end:")

# d=a.startswith(b)
# e=a.endswith(c)

# if d==True:
#     print("yes, your sentence begins with", b)
# else:
#     print("no, your sentence does not begin with", b)
# if e==True:
#     print("yes, your sentence ends with", c)
# else:
#     print("no, your sentence does not end with", c)

#################################################################
# ### Boolean Data Type Questions:
##################################################################

# # 1. Write a program that accepts a username and password and checks if both are not empty.
# a=input("username:")
# b=input("password:")
# c=bool(a)
# d=bool(b)
# if c==True and d==True:
#     print("you entered successfully to system!")
# if c==False or d==False:
#     print("Something wrong please enter username or password")

# # 2. Create a program that checks if two numbers are equal and outputs a message if they are.
# a=int(input("number1:"))
# b=int(input("number2:"))
# c=a-b
# if bool(c)==False:
#     print("numbers equal")
# else:
#     print("numbers different")

# # 3. Write a program that checks if a number is positive and even.
# a=int(input("number:"))
# if a>0 and a%2==0:
#     print("number is positive and even")
# if a<0 and a%2==0:
#     print("number is negative and even")
# if a>0 and a%2!=0:
#     print("number is positive and odd")
# if a<0 and a%2!=0:
#     print("number is negative and odd")

# # 4. Write a program that takes three numbers and checks if all of them are different.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# all_different = (a != b) and (a != c) and (b != c)

# print(all_different)

# # 5. Create a program that accepts two strings and checks if they have the same length.
# a=input("first:")
# b=input("second:")
# same_length= len(a)==len(b)
# print(same_length)

# # 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
# a=int(input('number:'))
# b= a%3==0 and a%5==0
# print(b)

# # 7. Write a program that checks if the sum of two numbers is greater than 50.
# a=int(input("first:"))
# b=int(input("second:"))
# greater= a+b>50
# print(greater)

# # 8. Create a program that checks if a given number is between 10 and 20 (inclusive)
# a=int(input('number:'))
# b= a>=10 and a<=20
# print(b)