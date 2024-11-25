def main():
    time = input("What time is it?")
    float_time = convert(time)

    if 7.00 <= float_time <= 7.59:
        print("breakfast time")
    elif 18.00 <= float_time <= 18.59:
        print("dinner time")
    elif 13.00 <= float_time <= 13.59:
        print("lunch time")

def convert(time):
    hours, minutes = time.split(":", 1)
    return int(hours) + (int(minutes) / 60)


if __name__ == "__main__":
    main()
