#
# def print_hi(name):
#        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# if __name__ == '__main__':
#     print_hi('PyCharm')

# Traversy crash course
# Variables
# x, y, name, is_cool = (1, 2.25, 'Hana', True)

# Basic Math
# a = x + y
# Casting => shaping
# x = str(x)
# y = int(y)
# z = float(y)

# print(x, y, name, is_cool)
# print(type(x))
# print(z)

#String Methods
# name = 'hana'
# age = 37

# Concatenate
# print('My name is' + name + 'my age is' + str(age))
# String Formatting
# Arguments by position
# print('My name is {name} and my age is {age}'.format(name=name, age=age))
# F-Strings
# print(f'My name is {name} and my age is {age}')

# s = 'hello world'
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(len(s))
# print(s.replace('world','everyone'))
# sub = 'h'
# print(s.count(sub))
# print(s.startswith('hello'))
# print(s.endswith('d'))
# print(s.split())
# print(s.find('r'))
# print(s.isalnum())
# print(s.isalpha())
# print(s.isnumeric())

# # LIST is a collection which is ordered & changeable. Allows duplicate memebers
# numbers = [1,2,3,4,5]
# fruits = ['Apples', 'Orange', 'Grapes', 'Pears']
# use a constructur
# numbers2 = list((1,2,3,4,5))
# print(numbers, numbers2)

# print(fruits[1])
# print(len(fruits))
# fruits.append('Mangos')
# fruits.remove('Grapes')
# fruits.insert(2, 'Strawberries')
# fruits.pop(2)
# fruits.reverse()
# fruits.sort()
# fruits.sort(reverse=True)
# fruits[0] = 'Blueberries'
# print(fruits)


# TUPLE is a collection which is ordered & unchangeable. Allows duplicate members


# fruits = ('Apples', 'Orange', 'Grapes', 'Pears')
# fruits2 = tuple(('A','B','C','D'))
# fruits2 = ('apo',)
# print(fruits[1])
# fruits[0] = 'gg' can't change it
# print(fruits, type(fruits2))
# del fruits2   to delete tuple
# print(fruits2)
# print(len(fruits))

# SET is a collection which is unordered & unindexed. No duplicate members
# vegs = {'A', 'B','C','E'}
# print(type(vegs))
# print('A' in vegs)
# vegs.add('MM')
# vegs.add('A')

# print(vegs)
# vegs.remove('MM')
# vegs.clear()
# del vegs
# print(vegs)

# Dictionary is a collection which is unordered, changeable & indexed. No duplicate members
# object
# person = {
#     'fname':'hana',
#     'lname':'shak',
#     'age':30,
# }
# person2 = dict(fname='sara',lname='williams')
# print(person2, type(person2))

# print(person['fname'])
# print(person.get('lname'))

# person['mobile']='0798888333'
# print(person)
# print(person.keys())
# print(person.items())

# person2 = person.copy()
# person2['city'] = 'amman'
# del(person['age'])
# person.pop('mobile')
# person.clear()
# print(len(person))
# print(person)

# List of dictionary
# people = [
#     {'name':'lala', 'age':30},
#     {'name': 'jojo', 'age': 25}
# ]
# print(people, type(people))
# print(people[1]['name'])

# Functions
# def sayHello(name):
#     print(f'Hello {name}')

# def sayHe(name='lala'):
#     print(f'Hello {name}')

# sayHe()
# sayHello('Hala')

# def getSum(num1, num2):
#     total = num1 + num2
#     return total
# num = getSum(3,4)
# print(num)

# Lambda Function (arrow function)
# getSum = lambda num1, num2 :num1 + num2
# print(getSum(10, 3))

# Conditionals
# x = 10
# y = 20

# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{y} is greater than {x}')
#
# if x > 2:
#     if x <= 10:
#        print(f'{x} is greater than 2 and less than or equal to 10')

# if x > 2 and x <= 10:
#        print(f'{x} is greater than 2 and less than or equal to 10')

# if x > 2 or x <= 10:
#        print(f'{x} is greater than 2 and less than or equal to 10')

# if not(x == y):
#     print('Not equal')

# Memebership operator
# r = 30
# members = [1,2,3,4,5]

# if r in members:
#     print(r in members)


# if r not in members:
#     print(r not in members)
# x=2
# y=9
# if x is y:
#     print(x is y)
#
# if x is not y:
#     print(x is not y, 'okkkk')

# Loop
people = ['lolo','soso','dodo','pop']
# for person in people:
#     print(f'Current Person: {person}')
#
# for person in people:
#     if person == 'soso':
#         break
#     print(f'Current Person: {person}')

#
# for person in people:
#     if person == 'soso':
#         continue
#     print(f'Current Person: {person}')

# range
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'{i}')

# count = 0
# while count <= 10:
#     print(f'Count: {count}')
#     count +=1

# Modules is a file containing a set of functions to include in your application.
# There are core python modules, modules can be install using the pip package manger
# including Django, as well as custom modules
import datetime
from datetime import date
import time
from time import time
from camelcase import CamelCase

import validator
from validator import validate_email

day = date.today()
today = datetime.date.today()
# timestamp = time.time()
tt = time()
c = CamelCase()
# print(c.hump('hello there world'))
# print(today)
# print(day)
# print(timestamp)
# print(tt)
email = 'test@test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is NOT valid')
