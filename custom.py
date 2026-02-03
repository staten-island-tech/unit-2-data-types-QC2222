def discount(isMember, age, isResident):
    if (age <= 12 or age >= 65):
        if(isMember == True or isResident == True):
            print("Discount applicable")
discount(True, 12, False)