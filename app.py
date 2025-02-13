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

# a = input("Verb 1=")
# b = input("Verb 2=")
# c = input("Noun 1=")
# d = input("Number 1=")
# e = input("Celebrity 1=")

# print(f"It was a {c} day out today. {e} wake up from his bed and start {a} his teeth. He was {d} years old now. After he finish washing his teeth, he go downstairs and start {b} his breakfast.")

# day_of_week = input("what day is it? ")
# if day_of_week == "Friday":
#     print("correct")
# else:
#     print("incorrect")


# def temp(Degrees):
#     if Degrees > 68:
#         print('warm')
#     elif Degrees == 68:
#         print('perfect')
#     else:
#         print('cold')
# x = int(input("What da temp"))


#integer, float, string, list, bollying...

# def degress(temp):
#     if temp > 68:
#         print("warm")
#     elif temp == 68:
#         print("perfect")
#     else:
#         print("cold")
# x = int(input("Temperature"))
# x(degress)

#Challenge 1    Let's create a function that determines if a number is odd or even

#Check if x is a factor moudlo 
#If factor == true add to list
#loop from 2 to y for i in range (2,15)
#if x isfactor and y isfactor then add to list 

# num = int(input("Number="))  
# def odd_even(num):
#     if num % 2 == 0:
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")

# odd_even(num)

#Challenge 2 Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 

# def service(rating, money):
#     if rating == "Good":
#         tip = 0.20
#     elif rating == "Great":
#         tip = 0.25
#     elif rating == "Okay":
#         tip = 0.15
#     elif rating == "Bad":
#         tip = 0

#     tip_amount = money * tip


#     print(f"Tip for {rating} service:{tip_amount}")

# rating = input("Rating:")
# money = float(input("Money:"))

# service(rating, money)






# service(rating, money)

# def service(rating, money):
#     if rating == "Good":
#         tip = 0.20
#     elif rating == "Great":
#         tip = 0.25
#     elif rating == "Okay":
#         tip = 0.15
#     elif rating == "Bad":
#         tip = 0
#     else:
#         return
#     tip_amount = money * tip
#     tip_amount= "Tip"


# rating = input("Rating (Good, Great, Okay, Bad): ")
# money = float(input("Bill amount: $"))

# service(rating, money)



# # Function to check if a number is a factor of another
# def is_factor(x, num):
#     return num % x == 0

# # Main logic
# def find_factors(m, y):
#     factors_list = []
    
#     # Loop from 2 to 14
#     for i in range(2, 15):
#         # Check if both m and y are divisible by i
#         if is_factor(i, m) and is_factor(i, y):
#             factors_list.append(i)

#     return factors_list










# # Example usage
# m = 99  # Replace with the number you want to check
# y = 30  # Replace with the other number to check for common factors

# # Check common factors
# common_factors = find_factors(m, y)
# print(f"Common factors of {m} and {y}: {common_factors}")

# # Test the odd/even function
# number_to_check = 10  # Replace with any number you'd like to check
# print(f"{number_to_check} is {is_odd_or_even(number_to_check)}")

# X = 
# Y = input("Number=")
# if X % Y == 0:
#     print(f"{Y} is a factor of {X}")
# else:
#     print(f"{Y} is not a factor of {X}")


# x = input("Type number here:")
# y = (12 % 5)
# y = (x)

# if y == True add to list
# elif y == False:
#     print("Odd")
  


#Challenge 3 Create a function that accepts an input and determines all factors of the number. 
# num = int(input("Number:"))

# def factor(num):  
#     factor_list = []  
#     for i in range(1, num + 1):
#         if num % i == 0:  
#             factor_list = factor_list + [i]
#     return factor_list 

# List = factor(num)
# print(f"Factors of {num}= {List}")

#Challenge 4 Create a function that accepts 2 arguments. Find the greatest common factor between those numbers. 
# X = int(input("First number="))
# Y = int(input("Second number="))
# def GCF(X, Y):
#     factor_list_X = []
#     factor_list_Y = []
#     for i in range(1, X + 1):
#         if X % i == 0:
#             factor_list_X = factor_list_X + [i]

#     for i in range(1, Y + 1):
#         if Y % i == 0:
#             factor_list_Y = factor_list_Y + [i]

#     gcf = 1  
#     for factor in factor_list_X:
#         if factor in factor_list_Y:  
#             if factor > gcf:  
#                 gcf = factor
#                 return gcf

        
# Z = GCF(X, Y)
        
# print(f"The GCF of {X} and {Y} is {Z}")

    



 