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

import random
letters = ['a', 'b', 'c', 'd', 'e']
numbers = ['1', '2', '3', '4', '5']
symbols = ['!', '@', '#', '%', '^']

print(' Welcome to my passward generator')

more_letters = int(input('how many letters would you like\n'))
more_numbers = int(input('how many numbers would you like\n'))
more_symbols = int(input('how many symbols would you like\n'))

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

password = []

for char in range(1, more_numbers + 1):
    random_char = random.choice(numbers)
    password += random_char

for char in range(1, more_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, more_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

random.shuffle(password)
print(f'your password is {password}')






