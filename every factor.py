x = input("Number")
x = int(x)
y = int(1)
if ((x % 2) == 0):
    for i in range(x + 1):
        if ((x % y) > 0):
            y = float(y + 1)
        elif  ((x % y) == 0):
            print(y)
            y = float(y + 1)
else:
    for i in range(x):
        if ((x % y) > 0):
            y = float(y + 2)
        elif  ((x % y) == 0):
            print(y)
            y = float(y + 2)