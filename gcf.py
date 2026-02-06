numbera = int(input("First number: "))
numberb = int(input("Second number: "))
currenttest = int(1)
currentgcf = int(0)
for i in range(max(numbera, numberb)+1):
    if ((numbera % currenttest) == 0 and (numberb % currenttest) == 0):
        currentgcf = currenttest
        currenttest = int(currenttest + 1)
    else:
        currenttest = int(currenttest + 1)
print(currentgcf)