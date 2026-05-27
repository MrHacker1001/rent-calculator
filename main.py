rent = int(input("Enter the rent amount:    "))
food = int(input("Enter the food expenses:    "))
electricity = int(input("Enter the electricity bill:    "))
charge_per_unit = int(input("Enter the charge per unit of electricity:    "))
person = int(input("Enter the number of people sharing the expenses:    "))

total_electricity = electricity * charge_per_unit
output = (rent + food + total_electricity) // person
print("Each person should pay:    ", output)
print("Total electricity bill:    ", total_electricity)
print("Total expenses:    ", rent + food + total_electricity)