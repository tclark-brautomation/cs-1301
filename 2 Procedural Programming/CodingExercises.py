# Logicals

# 2.2 Variables
from datetime import date
aNumber = -2
aNumber2 = 4
aDecimal = 7.1
aString = "Hello, world!"
aBoolean = True
aDate = date.today()

print(aNumber == aNumber2)
print(aNumber != aNumber2)
print(aNumber >= aNumber2)

# 2.3.3 Relational Operators
list_of_fruits = ["grape", "orange", "banana", "kiwi", "pear"]
search_fruit = "kiwi"

if search_fruit in list_of_fruits:
    print(True)
else:
    print(False)

#2.3.5 Boolean Operators
onList = True
inStock = True
onSale = False
rotten = False

print((onList or onSale)and inStock and not rotten)

