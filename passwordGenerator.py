import random

lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
specialSymbols = "@#$%^&*>?/-="

size = int(input("Enter the size of password: "))
allCharacters = lowerAlpha + upperAlpha + numbers + specialSymbols
passowrd = "".join(random.sample(allCharacters, size))
print(passowrd)
