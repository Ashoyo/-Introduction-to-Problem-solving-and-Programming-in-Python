date = input("Please enter a date")
month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:])
if month == 4 or month == 6 or month == 9 or month == 11:
    if 1 <= day <= 30:
        print("Valid Date")
    else:
        print("Invalid Date")
if month ==2:
    if 1<= day <= 31:
        print("valid Date")
    if day ==29:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("valid date")
                else:
                    print("Invalid Date")
            else:
                print("Invalid Date and not a leap year")
        else:
            print("Invalid Date")
if month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month ==10 
or month == 12:
    if 1 <= day <= 31:
        print("Valid Date")
    else:
        print("Invalid Date")
