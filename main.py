#print('Hello World') 
#print('world\nworld')
#print('Hello ' + input('what is your name?'))
#print(len(input('what is your name?')))

#a = input('a:')
#b = input('b:')


#c = a
#a = b
#b = c

#print(a)

#Data types

#strings
# print('hello'[3])
# print('123'+'697')

# num = len(input('what is your name?'))

# new_num = str(num)

# print('Your name has '+ new_num + ' characters' )


#2 digit calculator

# mad = input('give an input\n')
# man = int(mad[0])
# made = int(mad[1])
# print(man+made)



#BMI calculator

# weight = input('input body weight\n')
# height = input('input height\n')
# bmi = int(weight)/((float(height))**2)
# print(bmi)

# print(8//3)



#f-string

# score = 0
# height = 1.8
# isWinning = True

# print(f'your score is {score}, your height is {height}, you are winning is {isWinning}')


#Lifetime left

# age = input('input thy age:\n')
# years = 90 - int(age) 
# weeks = 52 * int(years)
# days = 365 * int(weeks)
# total = (f'you have {years} years, {weeks} weeks, {days} days left')
# print(total)


#conditionals

# print('WELCOME TO THE ROLLERCOASTER')
# height = int(input('Input your height:\n'))
# if height >= 120:
#  print('Hop in')
# else:
#  print('sorry')


# EVEN OR ODD NUM CHECK

# num = int(input('Input your number:\n'))
# if num % 2 == 0:
#     print('Even')
# else:
#     print('Odd')



#Rollercoaster age/height

# age = int(input('Input your age:\n'))
# height = int(input('Input your height:\n'))
# if age >= 18:
#     if height >= 120:
#         print('Welcome')
#     else:
#         print('Please leave')
# else:
#     print('Please leave')       



#BMI conditional calculator

# weight = int(input('input body weight\n'))
# height = float(input('input height\n'))
# bmi = weight/((height)**2)
# print(f"Your BMI is {bmi}")
# if bmi < 18.5:
#     print('under weight')
# elif bmi < 25:
#     print('Normal weight')
# elif bmi < 30:
#     print('overweight')
# elif bmi < 35:
#      print('obese')
# elif bmi > 35:
#     print('very fat')
# else:
#     print('error')





#change to lowercase

#print('USATA'.lower())


#count num of letters in a string

# print('USATA'.count("A"))


#love calculator
#input('')





#Random Module

# import random

# random_integer = random.randint(1,10) 
# print(random_integer)

# random_float = random.random() * 5

# print(random_float)




#Who is paying

# ok = input('input your names:\n')
# ohkay = ok.split(', ')
# print(ohkay)

# import random

# length = len(ohkay)
# random_num = random.randint(0, length-1)
# print(random_num)
# who_will_pay = ohkay[random_num]
# print(who_will_pay + ' is paying')




#test test

# import random
# test = random.randint(0,3)
# print(test)
# fruit = ['apple', 'orange', 'banana', 'pear']
# print(fruit[test])



#Rock, paper, scissors game





  #Loop

#for loop

# fruits = ['apple', 'orange', 'pineapple']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' juice')


#calculate mean height

# student_input = input('input height:\n').split()
 
# student_height = list(map(int, student_input))

# print(student_height)

# Total_height = sum(student_height)

# print(Total_height)

# num = len(student_height)

# final = (round(Total_height/num))
# print(final)



#calculate mean height using loop

# student_heights = input('input a list of height:\n').split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)


# total_height = 0
# for height in student_heights:
#     total_height += height
#     print(total_height)


# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)

# average_height = round(total_height / number_of_students)
# print(average_height)



# #test test test

# paste = input('put the numbers\n').split()
# for n in range(0, len(paste)):
#     paste[n] = int(paste[n])
# print(paste)


# add = 0
# for m in paste:
#     add = add + m
# print(add)


# div = add / len(paste)
# print(div)



# finding max number using loop

# okay = input('input\n').split()
# for o in range(0, len(okay)):
#     okay[o] = int(okay[o])
# print(okay)

# soap = 0
# for red in okay:
#     if red > soap:
#         soap = red
# print(soap)




# Range

# total = 0
# for number in range(1, 101):
#     total = total + number
# print(total)
 

# even = 0
# for eve in range(2, 101, 2):
#     even = even + eve
# print(even)



#fizzbuzz

# for num in range(0, 100):
#     if num %3 == 0:
#         print('fizz')
#     elif num %5 == 0:
#         print('buzz')
#     else:
#         print(num)





# passward generator

# import random
# letters = ['a', 'b', 'c', 'd', 'e']
# numbers = ['1', '2', '3', '4', '5']
# symbols = ['!', '@', '#', '%', '^']

# print(' Welcome to my passward generator')

# more_letters = int(input('how many letters would you like\n'))
# more_numbers = int(input('how many numbers would you like\n'))
# more_symbols = int(input('how many symbols would you like\n'))

#easy level

# password = ''

# for char in range(1, more_numbers + 1):
#     random_char = random.choice(numbers)
#     password += random_char

# for char in range(1, more_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for char in range(1, more_symbols + 1):
#     random_char = random.choice(symbols)
#     password += random_char

# print(password)



# hard

# password = []

# for char in range(1, more_numbers + 1):
#     random_char = random.choice(numbers)
#     password += random_char

# for char in range(1, more_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for char in range(1, more_symbols + 1):
#     random_char = random.choice(symbols)
#     password += random_char

# random.shuffle(password)
# print(f'your password is {password}')





#functions

# def my_function():
#     print('hello')
#     print('bye')

# my_function()



#while loop

# while number_of_hurdles > 0:
    # jump()
    # number_of_hurdles = number_of_hurdles - 1
    # print(number_of_hurdles)





# Hang man game

# word_list = ['ardvark', 'baboon', 'camel']

# import random

# chosen_word = random.choice(word_list)




# display = []
# for _ in range(len(chosen_word)) :
#     display += "_"
# print(display)


# guess = input('Guess a letter').lower()




# for letter in chosen_word:
#     if letter == guess:
#         print('Right')
#     else:
#         print('wrong')






# Functions with input

# def greet():
#     print('Hello')
#     print('How do you do')
#     print("Isn't the weather nice today")

# greet()


# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how do you do {name}?")

# greet_with_name("usata")





# functions with more than 1 input

# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")

# greet_with(name="Jane", location="Abuja")
#         #  or
# greet_with("Jane", "Abuja")





# Ceasar cipher

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#         print(f"The encoded text is {cipher_text}")

#         print(cipher_text)

# encrypt(plain_text=text, shift_amount=shift)








# Dictionaries

# programming_dictionary = {
#     "Bug": "an error in a code",
#     "functions": "A piece of code than can be easily called over",
# }

# adding items to dictionary

# programming_dictionary["Loop"] = "The action of doing someing over and over"


# to empty dictionary

# programming_dictionary = {}



# Loop through dictionary

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])





# Grading program

# student_scores = {
#     "Harry": 91,
#     "Ron": 88,
#     "Will": 71,
#     "Nash": 50,
# }


# student_grade = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grade[student] = "Exellent"
#     elif score > 80:
#         student_grade[student] = "Good"
#     elif score > 70:
#         student_grade[student] = "Not bad"
#     else:
#         student_grade[student] = "Fail"


# print(student_grade)     



# Nesting Lists and dictionaries

# travel_log = {
#     "France": {"cities_visited": ["paris", "Lille", "Dijon"], "total_visit": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }




# Secret Auction Program


# bid = {}
# bidding_finished = False 


# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""

#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#     name = input("what is your name?")
#     price = input("What is your bid? $")
#     bid[name] = price
#     should_continue =  input("Are there any other bidders? Type 'yes or no'.")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bid)
#     elif should_continue == "yes":
#         print("2")





# Functions with output

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format_name("angela", "ANGELA")



# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "you did not provide an input."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"

# format_name("angela", "ANGELA")



# # Calculator

# #Add
# def add(n1, n2):
#     return n1 + n2

# #Subtract
# def subtract(n1, n2):
#     return n1 - n2

# #Multiply
# def multiply(n1, n2):
#     return n1 * n2

# #Divide
# def divide(n1, n2):
#     return n1 / n2

# selector = {
#     "-":subtract,
#     "+":add,
#     "*":multiply,
#     "/":divide
#     }

# num1 = int(input("First number:\n"))
# num2 = int(input("Second number:\n"))
# for symbol in selector:
#     print(symbol)

# selector_symbol = input("Pick an operation from the line above:\n")

# cal_function = selector[selector_symbol]

# answer = cal_function(num1, num2)

# print(f"{num1} {selector_symbol} {num2} = {answer}")



# Black Jack



# your_card = random.choice(cards)
# print(your_card)


# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

# import random

# num1 = random.choice(cards)
# num2 = random.choice(cards)
# print(f'your cards are: {num1, num2}')


# # Computer

# com_num1 = random.choice(cards)
# com_num2 = random.choice(cards)
# print(f'computers first hand: {com_num1}')




# # Player

# new_card = input("Type 'y' to get a new card and 'n' to pass:\n").lower()

# new_num = random.choice(cards)

# if new_card == 'y':
#     print(f'your cards are now {(num1, num2, new_num)}')
# elif new_card == 'n':
#     print('fine')
# else:
#     print('invalid')

# print(f'The computers cards are now {(com_num1, com_num2)}')

# player_add = num1, num2, new_num
# sum_player = sum(player_add)
# print(f'Your total is: {sum_player}')

# com_add = com_num1, com_num2
# sum_com = sum(com_add)
# print(f'The computers total is: {sum_com}')

# one = 12
# two = 10
# num = one, two
# mid = sum(num)
# print(mid)

# # bid = (22, 22)
# # print(bid)


# if sum_player > sum_com:
#     if sum_player < mid:
#         print("You Win")
#     else:
#         print('Computer Wins')
# elif sum_com > sum_player:
#     if sum_com < mid:
#         print("Computer Wins")
#     else:
#         print("You Win")
# else:
#     print('No winner')





# Scope

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()


# Global Scope

# player_health = 10

# def drink_potion():
#     print(player_health)

# drink_potion()





# Debugging


# Describing the problem

# def my_function():
#   for i in range(1, 21):
#       if i == 20:
#         print("you got it")
# my_function()


# Reproduce the Bug

# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


# Play computer

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("you are a millenial")
elif year > 1994:
  print("you are a Gen Z.")


# Debugging with pythonTutor


