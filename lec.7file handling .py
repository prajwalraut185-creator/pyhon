# file = open("film.file.py", "r")
# data = file.read(18)
# print(data)

# f = open("film.file.py", "r")
# data = f.read()
# print(data)
# f.close()

# f  = open("film.file.py", "r")
# line2 = f.readline()
# print(line2)
# f.close()

# FILE "W" write mode  # val change

# f = open("film.file.py", "w")
# f.write("i we want to the everyrthing possible")
# f.close()

# f = open("film.file.py", "w")
# f.write("\n everything is possible if i want")
# f.write("\n thats make common resources provide happen you kind")
# f.close()

#  FILE CREATE EASY TRICK

# f = open("film.file.py", "a")
# f.write("\n my be common resources provided")
# f.close()

# R +  MODE 9( chije overwrite hote hai senteces ke aage lg jate hai

# f = open("film.file.py", "r+")
# f.write("\n do you understand i speak")
# print(f.read())
# f.close()
7
# WItH SYSNTAX
# WITH OPEN "DEMO TXT", "A") AS F :
 
# which is with syntax uses DATA = F.READ # automatically close hote

# with open("film.file.py", "r") as f:
#     data = f.read()
#     print(data)

# with open("film.file.py", "w") as f:
#     f.write("do you have a 100 rupees")
#     print()

# DELTING FILE 
# USING A OS MODULE # hm kisi bhi file ko delete kr skkte hai

# import os

# os.remove("create important.py")

# PRACTICE QUESTION
# create anew file "practice txt" using python. add the followoing in it

# ACCRODING TO ME
# file = open("cool file.py", "a+")
# file.write("\n a may i got of our way")
# file.close()

# MAIN ANSWER
# with open("create a file", "w") as f:
#     f.write("\ hello, i am a prajwal raut")

# waf that replaced occurrences of "java" with "pyhton" in above file

# with open("film.file.py", "a+") as f:
    # data = "common resources provide all time"
    # f.write(data)
    # print(data)

# new_data = data.replace("common resources provide all time", "my name is prajwal raut")
# print(new_data)
# f.close()

# search if  the word "learning" exist in the file or not
# != -1 not equal mtlb nhi mila

# with open("film.file.py", "r") as f:
#     data = f.read()
#     if(data.find("python programming") != -1):
#         print("found at a word")
#     else:
#         print("not found thid word")
   
#  WRITE TO QUESTION WHICH LINE OF THE FILE DOES WORD "LEARNING"
# OCCUR FIRST 
#PRINT -1 IF WORD NOT FOUND

# def check_for_line():
#     word = "him"
#     data = True
#     line_no = 1
#     with open("film.file.py", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()
        
# FROM A FILE CONTAINING NUMBERS SEPARATED BY COMMA. PRINT THE COUNT OF
# EVEN NUMBER.
# split mean in marathi todane
# MAIN ANS THIS QUESTION

# count = 1
# f = open("film.file.py", "r")
# data = f.read()

# num = data.split(",")
# for val in num:
#     if(int(val) % 2 == 0):
#         count += 1

# print(count)


