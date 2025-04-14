import random

# Question : 1

for num in range(1500,2701):
    if (num % 5 == 0 and num % 7 == 0):
        print(num)

# Question :  2

def celToFahren (num1):
    print ((num1 * 9/5) + 32)

celToFahren(60)
print()

def FahrenTocel (num1):
    print ((num1 - 32) * 5/9)

FahrenTocel(45)
print()


# Question :  3

def randomNum():
    a= random. randint(1, 9) 
    print(a)
    while True :
        userValue = int (input("Enter a Number : "))
        print(userValue)

        if(a == userValue):
            print("Well Gussed !")
            break
        else :
            print("Try Again !")

randomNum()



# Question :  4

def pattern():
    for i in range(10):
        for j in range(i):
            print('*', end="")
        print('')

pattern()


# Question : 5
def reverse_word(word):
    return word[::-1]

word = input("Enter a word: ")
print("Reversed word:", reverse_word(word))


# Question : 6

def counting(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even, odd = counting(numbers)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)


# Question : 7

def print_item_type(data_list):
    for item in data_list:
        print("Item:", item, "Type:", type(item))
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
print_item_type(datalist)



# Question :  8

for i in range ( 7 ) :                          
    if(i == 3 ):
        continue
    if(i==6):
        continue
    print(i)


# Question no 9

a, b = 0, 1
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b
    
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i) 

    # Question no 10  

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

result = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    result.append(row)

print("Generated 2D array:")
print(result)

# Question no 11

print("Enter lines of text (press Enter on an empty line to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())

print("\nOutput:")
for l in lines:
    print(l)

# Question no 12
binary_input = input("Enter comma-separated 4-digit binary numbers: ")

binary_numbers = binary_input.split(',')

for b in binary_numbers:
    if len(b) != 4 or any(char not in '01' for char in b):
        print(f"Invalid input: '{b}' is not a 4-digit binary number.")
        exit()
        
divisible_by_5 = []
for b in binary_numbers:
    decimal = int(b, 2)
    if decimal % 5 == 0:
        divisible_by_5.append(b)

print("Numbers divisible by 5:")
print(','.join(divisible_by_5))

# Question no 13

user_input = input("Enter a string: ")

letters = 0
digits = 0

for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)


# Question : 14

import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True


password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid Password")
else:
    print("Invalid Password")