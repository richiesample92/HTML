billtotal = 210

discount1 = 10
discount2 = 20

if billtotal > 100 and billtotal < 200:
    print("Bill is greater than 100!")
    billtotal = billtotal - discount1
elif billtotal > 200:
    print("Bill is greater than 200!")
    billtotal = billtotal - discount2
else:
    print("Bill is less than 100!")

print("total bill: " + str(billtotal))
