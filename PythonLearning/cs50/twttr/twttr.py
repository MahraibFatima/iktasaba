string = input("Input: ")
vowels = ['A', 'E', 'I', 'O','U','a','e','i','o','u']
string = [letter for letter in string if letter.lower() not in vowels]
string = ''.join(string)
print("Output:",string)
