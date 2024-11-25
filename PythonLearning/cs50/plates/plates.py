def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False

    if not (2 <= len(s) <= 6):
        return False

    if any(c in ". ,!@#$%^&*()+=<>?" for c in s):
        return False

    if not s[-1].isdigit() or s[0] == '0' or any(c.isdigit() for c in s[:-1]):
        return False

    return True

main()
