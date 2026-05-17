# fuction defination
# first method
# def calc_sum(a,b):
#     sum = a + b
#     print(sum)
#     return

# calc_sum(7,9)
# calc_sum(98,78)
# calc_sum(978,675)
         

# defination second method
# def calc_facto(a,b):
#     facto = a*b
#     print(facto)
#     return

# calc_facto(12,3)
# calc_facto(90,98)

# def print_hiiprajwal():
#     print("hiiprajwal") 
    

# print_hiiprajwal()
# print_hiiprajwal()
# print_hiiprajwal()

# def calc_avg(a,b,c,d,e,f,):
#     sum = a + b + c + d + e + f
#     avg = sum/6
#     print(avg)
#     return avg

# calc_avg(80,82,83,84,86,84)

#built-in function # print, len, type, sum
#under print function 
# print function

# print("apple", end = "")
# print("banana", end = "")
# print("orange", end = "")

# len fuction

# n = [1,23,45,6,7,6,6,9,0]
# print(len(n))

# n = (1,23,4,457,5)
# type fuction
# print(type(n))

#range function # range mean = jo sequences ke sath column form me.

# nums = [1,2,3,4,5,6]
# for i in range(len(nums)):
#     print(i, nums [i])

# num = [1,4,5,6,7,8,9]
# i = 0 
# while i < len(num):
#     print(i, num[i]) 
#     i += 1

# deafault parameter

# def calc_product(a=12, b=3):
#     print(a * b)
#     return

# calc_product()
    

# LETS PRACTICE
# wap to print the length of a list.(list is the parameter)

# cities = ["umred" , "nagpur", "mumbai", "pune", "delhi"]
# fruit = ("apple", "banana", "watermelan", "mango", "pineapple", "orange", "email" )

# def print_list(list):
#     print(len(list))

# print_list(cities)
# print_list(fruit)

# wap to print the element of a list in a single line.(list is the parameter)
# movies = ["dhuramndhar", "animal", "cat", "mat", "sta"]
# anythings = ["prajwal", "raut", "sacrifide", "opprtunities", "authoriry"]


# def print_list(list):
#     for item in list:
#         print(item, end = "")
#     print()

# print_list(movies)
# print_list(anythings)

# waf to find the factorial of n.(n is the parameter)
# def calc_facto(a):
#     facto = 1
#     for i in range(1, a+1):
#         facto = facto * i
#     print(facto)

# calc_facto(5)
# wap to converter  usd to inr

# def clac_converter(usd_doller):
#     inr_rs = usd_doller * 92
#     print(inr_rs , "inr", usd_doller, "usd")

# clac_converter(10)

#check even and odd number

# def bagh(a,b):
#     if(a % 2 == 0):
#         print(a, "even number")
#     else:
#         print(b, "odd number")
#     if(b % 2 == 0):
#         print(b, "even number")
#     else:
#         print(b, "odd number")

# bagh(12,19)

# recursion print_list(list, idx=0): 
#  recursion

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("pr")

# show(12)

# factorial
# def fact(n):
#     if(n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(89))
    
#sum

# def calc_sum(n):
#     if(n == 0):
#         return 1
#     return calc_sum(n-1) + n

# sum = calc_sum(15)
# print(sum)

#define to calculate the sum of first n natural numbers.

# def calc_sum(n):
#     if(n == 0):
#         return 1
#     return calc_sum(n-1) + n

# sum = calc_sum(12)
# print(sum)

#  fuction to print all element in list

# hint: use list & index as parameters(4

# name = ("king", "does", "become", "ahead", "and so on")
# sentences = ("some", "anywhere", "all about", "and so on")

# print_list(name)
# print_list(sentences)
# def print_list(list, idx=0):
#     if(idx, len(list)):
#      return
#     print(list, [idx])
#     print_list(list, idx+1)


