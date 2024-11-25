months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ")
        if '/' in date:
            parts = date.split('/')
            month_str, day_str, year_str = parts
        else:
            parts = date.split(' ')
            month_str, day_str, year_str = parts

        if(month_str in months):
            month = months.index(month_str.capitalize()) + 1
        #else:


        day = int(day_str.rstrip(','))
        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError

        year = int(year_str)

        print(f"{year}-{month:02d}-{day:02d}")
        break
    except ValueError:
        #print(ve)
        continue
