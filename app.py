# # #Strings are for representing characters, names, words, etc...
# # name = "David"
# # #Intergers represent whole numbers
# # age: 14
# # #Floats represent decimals
# # wallet  = 5.45
# # #Boolean represents true or false, used in evaluations
# # graduated = False

# # def add(x,y):
# #     print(x + y)
#     #input asks the user a question and stores their response as a value
# bill = float(input("What was the bill"))
# # #print(type(bill))
# # add(40, bill)


# lists
# students = ["Joanna, "David", "Deivid", "Other David", "Ethan"]
#             #similar to saying for i in range(5) : print(students[i]
# for student in students:
#     print(student) 

# moneys = [1,2,3,4,5,6]
# total = 0
# for money in moneys:
#     total = total + money
#     print(total)

# x = 3
# y = float(3)
# print(x,y)

# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i)

# print(values[0])
# print(values[6])

# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)

# Step 1: Get input from the user
bill = float(input("100.0"))  # Convert input to float
tip = int(input("6.6 "))  # Convert input to integer

# Step 2: Calculate the tip and total
tip_amount = bill * tip / 100  # Calculate the tip
total = bill + tip_amount  # Calculate the total

# Step 3: Print the result
print("Tip: $", round(tip_amount, 2))
print("Total: $", round(total, 2))

