# fuction defination
# first method
# def calc_sum(a , b): # (a,b) parameters
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(12,3) #function call , (1,2) arguments
# calc_sum(23,5)
# calc_sum(90,98)

# defination second method

# def calc_facto(a,b):
#     facto = a * b
#     return facto 

# facto = calc_facto(2, 3) 
# print(facto)


# def print_hello():
#     print("hello")

# print_hello()
# print_nums = 
# print_hello()

# def calc_avg(a,b,c,d,e,f):
#     sum = a + b + c + d + e + f
#     avg = sum / 6
#     print(avg)
#     return avg#average of 3 numbers

# calc_avg(56,78,89,65,43,67)

#built-in function
#under print function 

# print("apple", end = "")        #sep = " "
# print("banana" , end = "")       # "/n" blacshashon  mtlb next line me
# print("orange", end = "")

#len function
# nums = [1,2,3,4,5,6]

# print(len(nums))


# type function
#range fuction
# nums = [1,2,3,4,5,6,7,8,9]
# for i in range(len(nums)):
#     print(len(nums))

#deafault parameter

# def calc_product(a=9, b=4):
#     print (a * b)
#     return a * b

# calc_product()

# LETS PRACTICE
# wap to prin the length of a list.(list is the parameter)

# cities = ["umred" , "nagpur", "mumbai", "pune", "delhi"]
# fruit = ("apple", "banana", "watermelan", "mango", "pineapple", "orange")

# def print_len(list):
#     print(len(list))

# print_len("cities")
# print_len("fruit")

# wap to print the element of a list in a single line.(list is the parameter)

# movies = ["manv", "kgf"," dhurandhar", "pushpa", "bahubali"]
# game = ["fre fire","pubg", "subway", "temple run", "call duaty"]

# def print_list(list):
#     for item in list:
#         print(item, end = " ")
#     print()

# print_list(movies)
# print_list(game)
    
# waf to find the factorial of n.(n is the parameter)

# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# calc_fact(5)

#wap to convert usd to inr

# def converter(usd_val):
#     inr_val = usd_val * 91
#     print(usd_val, "usd =", inr_val, "inr")

# converter(34)

# def find_number(a,b):
#     if a % 2 == 0:
#         print(a, "even number")
#     else:
#         print(a, "odd number")
#     if b % 2 == 0:
#         print("even number")
#     else:
#         print("odd number")
    
#     find_number(12,76)

# recursion

def show(n):
    if(n == 9): #base
        return
    print(n)
    show(n-1)

show(100)

