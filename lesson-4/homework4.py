# ## Questions:

# 1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
# 20 correct answer out of 25
# 2.  What is the difference between the continue and break statements in Python?
# the continue statement id used to stop loop in certain condition, but loop continues in different values, while break will stop loop totally
# 3. Can you explain the difference between for loop and while loop?
#  for loop is used to make operations on every member of iterable objects, on the other hand, while loop is executed when certain conditions meet
# 4. How would you implement a nested for loop system? Provide an example.
# nested for loop is used to make operation in 2 or more iterable objects.
# for example if task asks me to execute numbers from 1 to 10 with every number in that range i would use nested loop
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i , j)
###################################
# # **1.** Return uncommon elements of lists. Order of elements does not matter.

# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]



# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]



# input:
#     list1 = [1, 1, 2, 3, 4, 2]
#     list2 = [1, 3, 4, 5]
# output: [2, 2, 5]

# # solution
# list1 = [1, 1, 2]
# list2 = [2, 3, 4]

# output=[]
# for i in list1:
#     if i not in list2:
#         output.append(i)

# for j in list2:
#     if j not in list1:
#         output.append(j)
# print(output)

# ############################
# # **2.** Print the square of each number which is less than `n` on a separate line.

# # input: n = 5
# # output:
# #     1
# #     4
# #     9
# #     16

# # solution
# n=5
# for i in range(1, n):
#     print(i**2)

# **3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.


# input: hello
# output: hel_lo



# input: assalom
# output: ass_alom



# input: abcabcdabcdeabcdefabcdefg
# output: abc_abcd_abcdeab_cdef_abcdefg

#    solution
# txt = "abcabcdabcdeabcdefabcdefg"
# unlilar = "aeiou"

# result = ""
# count = 0
# i = 0

# while i < len(txt):
#     result += txt[i]
#     count += 1

#     # agar oxirgi belgi bo‘lsa — chiziqcha yo‘q
#     if i == len(txt) - 1:
#         break

#     if count == 3:
#         # agar unli bo‘lsa yoki oldingi qismda _ bo‘lgan bo‘lsa
#         if txt[i] in unlilar or result.endswith("_"):
#             # keyingi harfdan keyin qo‘yiladi
#             i += 1
#             if i < len(txt):
#                 result += txt[i]
#                 result += "_"
#             count = 0
#         else:
#             result += "_"
#             count = 0

#     i += 1

# print(result)

# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning
# # solution
# import random

# while True:
#     secret_number = random.randint(1, 100)
#     attempts = 10

#     print("\n🎮 Number Guessing Game")
#     print("I have selected a number between 1 and 100.")
#     print("You have 10 attempts to guess it.")

#     while attempts > 0:
#         guess = int(input(f"\nAttempts left {attempts}. Enter your guess: "))

#         if guess > secret_number:
#             print("Too high!")
#         elif guess < secret_number:
#             print("Too low!")
#         else:
#             print("🎉 You guessed it right!")
#             break

#         attempts -= 1

#     # If attempts are over and number was not guessed
#     if attempts == 0:
#         print("\n❌ You lost. Want to play again?")

#     # Ask to play again
#     choice = input("Type Y / YES / y / yes / ok to play again: ").lower()

#     if choice not in ['y', 'yes', 'ok']:
#         print("Thanks for playing! 👋")
#         break

# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."

# solution

# while True:
#         password = input(f"\nCreate your password: ")

#         if len(password) < 8:
#             print("Password is too short.")
#         elif password.islower() :
#             print("Password must contain an uppercase letter.")
#         else:
#             print("Password is strong.")
#             break

# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and
#  itself. Use nested loops to check divisibility.
# solution
# for num in range(2, 101):          # numbers from 2 to 100
#     is_prime = True               # assume number is prime

#     for i in range(2, num):       # check divisibility
#         if num % i == 0:
#             is_prime = False
#             break                 # not prime, stop checking

#     if is_prime:
#         print(num)

# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# # - Display the winner and keep track of scores for the player and the computer.
# # # # - First to 5 points wins the match.
# import random
# while True:
#     comp_score=0
#     player_score=0
#     print("Game R S P")

#     while comp_score<5 and player_score<5:
#         pl=input("your choice R S P:").capitalize()
#         cp=random.choice(['R', 'S', 'P'])
#         print(pl)
#         print(cp)
#         if pl==cp:
#             print('this is a tie')
#         elif (pl == 'R' and cp == 'S') or \
#              (pl == 'S' and cp == 'P') or \
#              (pl == 'P' and cp == 'R'):
#             player_score+=1
#         else:
#             comp_score+=1
#         print( "your score:", player_score, "comp score:", comp_score,)
#     if comp_score==5:
#         print("you lost")
#         break
#     if player_score==5: 
#         print("you win") 
#         break

