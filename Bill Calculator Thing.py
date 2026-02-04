x = float(input("Bill value? "))
servicelevel = input("Was the service bad, okay, good, or great?")
if (servicelevel == "bad"):
    print("tipped 0%")
    finalbill = str(x)
    print("Final Bill " + "$" + finalbill)
elif (servicelevel == "okay"):
    print("tipped 15%")
    finalbill = str(x * 1.15)
    print("Final Bill " + "$" + finalbill)
elif (servicelevel == "good"):
    print("tipped 20%")
    finalbill = str(x * 1.2)
    print("Final Bill " + "$" + finalbill)
elif (servicelevel == "great"):
    print("tipped 25%")
    finalbill = str(x * 1.25)
    print("Final Bill " + "$" + finalbill)