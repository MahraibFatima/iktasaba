while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split('/', 1)
        x, y = int(x), int(y)
        if(x>y):
            raise ValueError
        result = round((x / y) * 100)
        if(result >= 99):
            print("F")
        elif(result <= 1):
            print("E")
        else:
            print(f"{result}%")
        break
    except (ValueError, ZeroDivisionError):
        continue
