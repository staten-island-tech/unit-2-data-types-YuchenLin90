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


# #lists
# # students = ["Joanna, "David", "Deivid", "Other David", "Ethan"]
# #             #similar to saying for i in range(5) : print(students[i]
# # for student in students:
# #     print(student) 

# moneys = [1,2,3,4,5,6]
# total = 0
# for money in moneys:
#     total = total + money
#     print(total)

# x = 3
# y = float(3)
# print(x,y)

#Tip Conculator
# X = input("Bill=")  
# Y = input("Tip=")  

# X = float(X) 
# Y = int(Y)  

# Y = X * (Y / 100)  
# Z = X + Y 

# print(f"Bill: ${X}, Tip: ${Y}, Total: ${Z}")


# values = [1,2.23,5,7,2,30,15,8]
# print(values)
# for i in values:
#     print(i)

# print(values[7])

# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)

#Challenge 1
#First, use the input to ask the user to input a sentence. (Like the first and second part of the tip conculator.)
#Second, create/write a function that could help counting the words in the sentence. (Remember to use string.)
# x = input("Type here=")     
# def word_count(x):
#     y = x.split()
#     return len(y)
# y= word_count(x)
# print(f"Numer of words={y}")

#Quiz next week about 6 statements/datatypes and evaluate them.


#Mab Libs Project 

a = input("Verb 1=")
b = input("Verb 2=")
c = input("Noun 1=")
d = input("Number 1=")
e = input("Celebrity 1=")

print(f"It was a {c} day out today. {e} wake up from his bed and start {a} his teeth. He was {d} years old now. After he finish washing his teeth, he go downstairs and start {b} his breakfast.")

