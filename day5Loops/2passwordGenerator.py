#Password Generator Project
import random
import secrets
from tkinter import N
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_letter=[]
total_number=[]
total_symbol=[]
for letter in range(0,nr_letters):
    total_letter+=secrets.choice(letters).split()
for symbol in range(0,nr_symbols):
    total_symbol+=secrets.choice(symbols).split()
for number in range(0,nr_numbers):
    total_number+=secrets.choice(numbers).split()
str_letter=''.join(total_letter)
str_number=''.join(total_number)
str_symbol=''.join(total_symbol)
str_password=str_letter+str_number+str_symbol
s=''.join(random.sample(str_password,len(str_password)))
print(s)
