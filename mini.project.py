# pyhton restourant
# menu = {
#     "samosa" : 60,
#     "dosa" : 50,
#     "pizza" : 40,
#     "burger" : 60,
#     "vadapav" : 90
# }
# print("welcome the python restourant")
# print("\n samosa : 60 \n dosa : 50 \n pizza : 40 \n burger : 60 \n vadapav : 90")

# total_ammount = 0
# # first item order

# item_1 = input("tumala kotna item pahije = ")
# if item_1 in menu:
#     total_ammount += menu[item_1]
#     print(f"ha {item_1} item aahe menu mdhi aahe")

# else:
#     print(f"nahi aahe {item_1} ha item")

# print(f"total ammount {total_ammount}")

# #second item order
# item_2 = input("tumala punha item pahije ky (ho/nahi)= ")
# if item_2 == "ho":
#     item_2 = input("konta item pahije = ")
#     total_ammount += menu[item_2]
#     print(f"ha{item_2} item aahe menu mdhi")

# else:
#     (f"ha item{item_2} jr aahe tr aan")


# print(f"tumhi je ghetl tyanch purn payment {total_ammount}")


# PROJECT 2 🎉🎉🎉🎉

# import random

# secret_number = random.randint(1, 10)

# while True:

#     guess = int(input("enter number: "))

#     if guess == secret_number:
#         print("correct !")
    
#     elif guess == secret_number:
#         print("high number")

#     else:
#         print("low number")

# PROJECT 3 

# import random

# secret_number = random.randint(1, 10)

# attempt = 0
# max_attempt = 5


# while attempt < max_attempt:
#     guess = int(input("enter number: "))

#     if guess == secret_number:
#         print("win🎉🎉")
#         break

#     elif guess > secret_number:
#         print("high👆👆")
    
#     else:
#         print("low👇👇")

# print("Remaining chance: ", max_attempt - attempt)
# if guess != attempt:
#     print("game over⛔⛔")
    

# with open("prajwal.py") as f:
 
#     for line in f:
#         print(line)

# f.close()

# POJECT 

course = str(input("enter class: "))
name = str(input("enter name: "))
mark = int(input("enter mark: "))
mothername = str(input("enter mother name: "))

percentage = (mark / 900) * 100
print(percentage)

if percentage > 90:
    print("GRADE A")
elif percentage >= 75 and percentage <= 90:
    print("GRADE B")
elif percentage >= 60 and percentage <= 75:
    print("GRADE C")
elif percentage >= 35 and percentage <= 60:
    print("GRADE D")
else:
    print("FAIL")

student = []

student_data = {
    "course" : course,
    "name" : name,
    "mothername" : mothername,
    "mark" : mark,
    "percentage" : percentage,

}

student.append(student_data)

print(student_data)