year = int(input("Enter your expacted year:"))

if year % 100 != 0 and year % 4 == 0:
    print("Exactly leep year!")

else:
    print("NO! this year is not a leep year.")