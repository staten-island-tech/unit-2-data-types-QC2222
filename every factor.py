x = int(input("Number"))
y = int(1)
for i in range(x + 1):
    if ((x % y) == 0):
        print(y)
    y = (y + 1)