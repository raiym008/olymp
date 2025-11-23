n = int(input())

if n >= 1 and n < 3 or n == 12:
    print("Winter")
elif n >= 3 and n < 6:
    print("Spring")
elif n >= 6 and n < 9:
    print("Summer")
elif n >= 9 and n <= 11:
    print("Autumn")
else:
    print("Error")