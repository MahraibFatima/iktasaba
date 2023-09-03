num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("""SELECT an arithmetic operator:
           
'+': for Addition
'-': for Subtraction
'*': for Multiplication
'/': for Division
'%': for Remainder
'//': for Modolus
'**': for Exponent

op = """)

if(op == '+'):
    print(f"Result of {num1} + {num2} is: {num1 + num2}")
elif(op == '-'):
    print(f"Result of {num1} - {num2} is: {num1 - num2}")
elif(op == '*'):
    print(f"Result of {num1} * {num2} is: {num1 * num2}")
elif(op == '/'):
    print(f"Result of {num1} / {num2} is: {num1 / num2}")
elif(op == '%'):
    print(f"Result of {num1} % {num2} is: {num1 % num2}")
elif(op == '//'):
    print(f"Result of {num1} // {num2} is: {num1 // num2}")
elif(op == '**'):
    print(f"Result of {num1} ** {num2} is: {num1 ** num2}")
else:
    print("Invalid operator!!")