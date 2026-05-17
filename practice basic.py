# Q.1# a = int(input("eneter number: "))

# square = a * a
# print(square)

# Q2 # num = int(input("enter number: "))

# if num % 2 == 0:
#     print("even")

# else:
#     print("odd")

# Q 3

# num = int(input("enter number: "))

# if num > 0 :
#     print("positive")

# elif num < 0:
#     print("negative")

# else:
#     print("zero")

# Q4

# num = int(input("enter number: "))
# total = 0
# i = 1
# while i < num:
#     total = total + i
#     i += 1

# print("sum is", total)

# num = int(input("enter number: "))

# count = 1
# for i in range(1, num + 1):
#     print(i)
#     count = count + i

# print("sum is:", count)

# n = int(input("enter number: "))

# i = 1
# facto = 1
# for i in range(1, n * 1):
#     print(i)
#     facto = facto * i

# print("facto =", facto)

# n = int(input("enetr number: "))

# facto = 1
# i = 1
# while i <= 5:
#     print(i)
#     facto = facto * i
#     i += 1

# print("facto is =", facto)


# Q5 # @staticmethod

# def sum(a,b,c,d):
#     abcd = a * b * c * d
#     return abcd

# s1 = sum(34,78,9,56)
# print(s1)

# Q6 # a = int(input("enter number: "))
# b = int(input("enter number: "))
# c = int(input("enter number: "))
# d = int(input("enetr number: "))
# e = int(input("enter number: "))

# if a > b and a > c and a > d and a > e:
#     print("he sglyat mothi aahe =", a)

# elif  b > c and b > d and b > e:
#     print("sglyat mothi he aahe =", b)

# elif c > d and c > e:
#     print("he sglyat mothi aahe =", c)

# elif d > e:
#     print("sglyat mothi he aahe =", d)

# else:
#     print("sglyat mothi t hech aahe =", e)

# Q7
# n = int(input("enter number: "))

# count = 0
# i = 0
# while i < n:
#     if i % 2 != 0:
#         print(i)
#     count = count + 1
#     i += 1

# print("total number odd:", count)

# n = int(input("enter number: "))

# count = 0
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         count = count + i

# print("total no odd:", count)

# Q8


# USING A WHILE LOOP

# n = int(input("enter number: "))
# i = 0
# sum = 0

# while i <= n:
#     print(i)
#     sum = sum + i
#     i += 1

# print("sum is:", sum)

# USING A FOR LOOP

# n = int(input("enter number: "))
# i = 0
# sum = 0
# for i in range(1, n + 1):
#     print(i)
#     sum = sum + i

# print("total is:", sum)

# Q9 METHODS OD list
# ADD = append, extend, insert
# x = [1,2,3,4,56,] # append mdhi 1 add kru shkto taku shkato.
# x.append(23)
# print(x)

# x = [11,34,56,]   # extend mdhi kiti add kru shkto
# x.extend([33,34])
# print(x)

# x = [1, 2, 3, 4]   # isert mdhi tyachya kru specefic thikani add shkto
# x.insert(1,5)
# print(x)

# # DELETE = remove, pop, clear

# x = [ 1,2,3,4] # pop tya idex vr joun delete krte
# x.pop(2)
# print(x)

# x = [1,2,3,4]  # remove ha tya number vr jaoun delete krte
# x.remove(1)
# print(x)

# x = [1,2,3,4]
# x.clear()
# print(x)

# # CHECK = index, count

# x = [1,2,3,4]       # ye index count krta hai
# print(x.index(3))
# print(x)

# x = [1,1,3,2]
# print(x.count(1))
# print(x)

# # arrange = sort and sort reverse =True
# x = [1,1,1,2,2,3,33,4]
# # 
# x = [1,2,3,3,3,4,4,5,5,6]
# x = [1,2,3,4,]  # assending order list print
# x.sort()
# print(x)

# x = [1,2,3,4]   # dessending order list print
# x.sort(reverse=True)
# print(x)

# # copy = copy

# x = [1,2,3,5]

# a = x.copy()
# print(a)

# # Q 10
# using exponenttiation

# square = int(input("enter number: "))

# square = square ** (1/2)

# print(square)

# using module
# import math

# sq = int(input("enter number: "))
# sq = math.sqrt(sq)
# print("the num of square root is =", sq)

# Q 11
# & calculate the area of traingle

# height = float(input("enter the height: "))
# base = float(input("enter the base: "))

# area = (1/2)*base*height
# print("the hieght of traingle", area)

# Q 12
# using temprary

# x = 5
# y = 6

# temp = x
# print("the value of temp vriable", temp)

# x = y
# print("value of the x is", x)

# x = y

# Q 13
# km to miles

# km = int(input("enter km: "))

# miles = (0.621371)*km
# print(km, "km dala maine", miles, "miles")

# Q 14
# using conditional statement

# n = int(input("enter number: "))

# if n < -1:
#     print("negative")

# elif n > 0:
#     print("positive")

# else:
#     print("zero")

# Q 14
# even and odd check

# n = int(input("enter number: "))

# if n % 2 == 0:
#     print("even")

# else:
#     print("odd")

# Q 15
# check a leap year

# y = int(input("enter number: "))

# if (y % 400 == 0) and (y % 100 == 0):
#     print("leap year")

# elif (y % 4 == 0) and (y % 100 != 0):
#     print("not a leap year")

# else:
#     print("not leap y")


#  = int(input("enter year: "))

# if (y % 400 == 0) and (y % 100 == 0):
#     print("leap year")

# elif (y % 4 == 0) and (y % 100 != 0):
#     print("he pn leap year")

# else:
#     print("not leap year")

#  CHECK THE LARGEST NUMBER

# a = float(input("enter number: "))
# b = float(input("enter number: "))
# c = float(input("enter number: "))

# if a > b and a > c:
#     print("a is largest number")

# elif b > c:
#     print("b is largest number")

# else:
#     print("c largest number")

# Q 16
# CHECK THE PRIME NUMBER

#  USINFNFOR LOOP

# n = int(input("enter number: "))

# if n <= 1:
#     print("not prime number")

# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("not prime number")
#             break

#     else:
#         print("prime number")


#  USING WHILE LOOP

# n = int(input("enter number: "))

# if n <= 1:
#     print("not prime number")

# else:
#     i = 2
#     while i < n:
#         if n % i == 0:
#             print("not prime number")
#             break
# Q 17

# import random

# n = random.randint(0,10000)

# print(n)

# PRINT ALL PRIME NUMBERS IN AN INTERVAL
# lower = int(input("enter number: "))
# upper = int(input("enter number: "))

# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# PRGRAM TO METER AND KELOMETER

# meter = float(input("enter number: "))

# kelometer = (meter * 1000)
# print(kelometer)

# SECOND METHOD IN CALCULATE THE FACTORIAL

# num = int(input("enter number :"))

# facto = 1

# if num < 0:
#     print("facto not exist")

# if num == 0:
#     print("facto is the", 1)

# if num > 0:
#     for i in range(1, num + 1):
#         facto = facto * i

# print("facto number is: ", facto)

# CLACULATE THE FACTORIAL USING RECURSION
# recursion mtlb vo khu hi ko call krta hai

# def div(a):
#     if a == 0:
#         return 1
#     else:
#         return(a) / div(a-1)
    
# num = int(input("enter number: "))
# ans = div(num)
# print("div is the", ans)

#  CREATE A TABLE OF USING TO FOR AND WHILW LOOP

# n = int(input("enter number: "))

# i = 1
# while i <= 10:
#     print(i**n)
#     i += 1

# n = int(input("enter number: "))

# for i in range(1, 20):
#     print(n, "x", i, "=", i*n ) 

# n = int(input("enter number: "))

# i = 1
# while i <= 10:
#     print(n, "x", i, n*i )
#     i = i + 1

# feconassi sequences created

# num = int(input("enter number: "))
# a =  12
# b = 3
# c = 9

# if num == 12:
#     print(a)

# else:
#     print(a)
#     print(b)
#     print(c)
#     for i in range(1, num+1):
#         d = a+b+c
#         a = b
#         b = c
#         c = d
#         print(d)

# PROGRAM TO CHECK AMSTRONG NUMBER

# num = int(input("enter number: "))

# num = 0
# temp = num

# while temp > 0:
#     digit = temp%10
#     cube = digit**3
#     sum = sum + cube
#     temp //= 10

# if sum == num:
#     print("amstrong number")
# else:
#     print("not amstrong number")

# PROAGRAM TO FIND ARMSTRONG NUMBER IN AN INTERVAL



# lower = int(input("enter number: "))
# upper = int(input("enter number: "))

# for num in range(lower, upper + 1):
#     order = len(str(num))
#     total = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** order
#         temp //= 10

#     if num == total:
#         print(num)
     
# LAMBDA FUCTION 

# sum = lambda a, b: a + b
# print(sum(12,12))

#  FILE HANDLING 

# with open("for.file.py", "r") as file:
#     data = file.read()
#     print(data)

# with open("for.file.py", "r+") as file:
#     print(file.read())
#     file.write(" n\ AAAAAAAAAAAAAAAA")


# with open("for.file.py", "w") as file:
#     file.write("print hello world")


# with open("for.file.py", "w+")
# file.write("i common resources provided is another sides")
# file.seek(3)
# file.read()

# FILE ADD AND FILE REMOVE

# with open("car.file.py", "x") as file: 
#     file.write("king")

# import os

# os.remove("snake_game.py")

# with open("prajwal.py", "a") as file:
#     data = file.write("prajwal")

# with open("prajwal.py", "a+") as file:
#     file.write("we geting the house working on morning ")
#     file.seek(2)
#     file.read()

# SETS

# a = [1,2,3,4]
# a.append([5])
# print(a)

# a = {1,2,3,4}
# a.update([50,60])
# print(a)

# a = [1,2,3,4]
# a.remove(3)
# print(a)

# a = {1,2,3,4} # element nhi hai to bhi eror nhi deta hai.
# a.discard(5)
# print(a)

# a = [1,2,3,4]  # radom delete
# a.pop()
# print(a)

# a = [1,2,3,45,5,]
# a.clea
# r()
# print(a)

# a = [1,2,3,4,5,6]
# b = [1,2,9,0,7,5,10,11,12,13]

# print(set(a).union(set(b)))

# a = [1,2,3,6,5,9]      # common element
# b = [3,8,7,6,4,9,5]

# print(set(a).intersection(set(b)))

# a = {1,2,3,4}       # unique value
# b = {1,2}

# print(set(a).difference(set(b)))

# x = {1,1,} # x me hua to true nhi hua t o false
# c = {2,4

# print(set(x).issubset(set(c)))

# define menu of restuarant

