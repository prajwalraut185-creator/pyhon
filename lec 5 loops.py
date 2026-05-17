#print number from 1 to 100 and print number from 1
# i = 100
# while i <= 10000:
#     print(i)
#     i += 1

#print the number from 890 to 101
  
# i = 1000
# while i >= 10:
#     print(i)
#     i -= 1

# print("loop ended")

#print the multification table of a number 

# i = 9
# while i <= 10:
#     print(i*19)
    # i += 1
    
# #print the element of following list using a loop :
# name = ("name", "country", "continent", "earth", "galaxy", "ambition", "bibligeography")

# idx = 2
# while idx < len(name):
#     print(name[idx])
#     idx += 1

#searh for a number x in this tuple using loop:
# mark = (78,89,98,98,89,78,95,95,94,93,92,91)
# x = 92
# i = 0
# while i < len(mark):
#     if(mark [i] == x):
#         print("sapdala re bhau", i)
#         break
#     else:
#         print("pahat aho n")
#     i += 1

# print("zala loop khatam")

# i se start     
# i = 1000
# while i <= 1:
#     if(i == 765):
#         print(i)
#     i += 1
    
#loops are used for sequential traversing list string list, string, tuples etc.

#for loops
#for el in list:
    #some work

#for loops with else 
#for element in  list:
      #some work

#else:
      #work when loop ends
        
# i = 0
# while i <= 100:
#     print(i)
#     i += 1

#ek element uthao aur kaam kro # for in charactar str

#lets practice
#print the element of the following list using a loop
  #[1, 2, 8, 9, 0, 8, 8, 9]

# nums = (1,2,3,4,3,2,1,9)

# num = (12,45,67,87,98,76,76,56,)
# x = 76
# idx = 0
# for el in num:
#     if(num [idx] == x):
#         print("sapdala la be it haye", idx)
#         break
#     else:
#         print("it pn nhi ahe re")
#         idx += 1

# DIFFERENCE ON WHILE LOOP AND FOR LOOP
# i = 0
# while i < 100: 
#     print(i)
#     i += 1
                       # SAME SAME BUT DIFFERENCE 
# for i in range(100):
#     print(i)

#RANGE( )
# range fuction returns a sequence of numbers, strating from 0 by default, and increments 
# by 1 (by deafault), and stops before a specified numbers.

# range(start?, stop , step ? ) start = kha se shuru nkrna hai 2 stop = kha tk ye number include nhi hota
                               #step = kitne gap se badahna hai
# for i in range(910):
#     print(i)

# for i in range(1,870,87):
#     print(i)

# n = int(input("enter number: "))
# i = 1
# while i <= 10:
#     print(i*n)
#     i += 1

# for i in range(2, 40, 5):
#     print(i)
    
# for i in range(1,30,2):
#     print(i)

# for i in range(2, 30, 2):
#     print(i)

#LET'S PRACTICE
#using for & range()
#print numbers from 1 to 100 & print numbers from 100 to 1

# for i in range(1,101):
#     print(i)

# for i in range(0 , 101, 1):
#     print(i)

#print multification table of a number n.

#WAP to find the some of first n numbers.(using while)
# n = int(input("enter number: "))
 
# for i in range(1,10):
#     print(i*10)
# 4*1*3

# n = int(input("eneter number: "))
# facto = 4
# i = 1
# while i <= n:
#     facto *= i
#     i += 1

# print("factorial =", facto)

# n = 4
# facto = 1
# i = 1
# while i <= n:
#     facto *= i
#     i += 1

# print("factorial =", facto)

# n = 9
# sum = 1
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("sum =", sum)

#wap to find the factorial of first numbers.(using for)
#while loop

# n = 9
# sub = 0
# i = 0
# while i <= n:
#     sub -= i
#     i += 1

# print("sub =", sub)

# this is a same process using a for loop
#for loop
# n = 777
# sum = 10
# for i in range(1, n+1):
#     sum += i

# print("sum =", sum)

# CALCULATOR DESIGN

a = int(input("enter number: "))
b = int(input("enter number: "))

print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. power")

choice = int(input("enter choice: "))

if choice == 1:
    print("choice", a + b)

elif choice == 2:
    print("choice", a - b)

elif choice == 3:
    print("choice", a * b)

elif choice == 4:
    print("choice", a / b)

elif choice == 5:
    print("choice", a ** b)

else:
    print("wrong choice")