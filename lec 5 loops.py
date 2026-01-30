#print number from 1 to 100 and print number from 1
# i = 10 
# while i <= 1000:
#     print(i)
#     i += 1

 
#print the number from 890 to 101
  
# i = 1000
# while i >= 10:
#     print(i)
#     i -= 1


#print("loop ended")

#print the multification table of a number 
# n = int(input("enter number: "))
# i = 10
# while i <= 10:
#     print(n*10)
#     i += i

#print the element of following list using a loop :
# name = ("prajwal", "king", "badshah", "attitude", "alpha")
# idx = 2
# while idx < len(name):
#     print(name[idx])
#     idx += 1

#searh for a number x in this tuple using loop:
# mark = (23, 45, 67, 78, 98, 67, 34,)
# x = 34
# i = 0
# while i < len(mark):
#     if(mark [i] == x):
#         print("found at mark", i)
#         break
#     else:
#         print("finding")
#         i += 1

# print("end of loop")

# i se start      
# i = 1
# while i < 1000:
#     if(i == 99):
#         print(i)
#     i += 1 
# print("end of loop")

# i = 100
# while i <= 1:
#     print(i)
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
# while i < 100:
#     print(i)
#     i += 1

#ek element uthao aur kaam kro # for in charactar str
# str = "prajwal raut"
# for char in str:
#     if(char == 'u'):
#         print("u found")
#         print("char")
# else:
#     print("end")
        
#lets practice
#print the element of the following list using a loop
  #[1, 2, 8, 9, 0, 8, 8, 9]

# nums = (1,2,3,4,3,2,1,9)

# for el in nums:
#     print(el)

# nums = (1, 2, 3, 9, 3, 6)
# x = 6
# idx = 0
# for el in nums:
#     if(el == x):
#         print("found at a idx", idx)
#     idx += 1
# else:
#     print("end")
        

#RANGE( )
# range fuction returns a sequence of numbers, strating from 0 by default, and increments 
# by 1 (by deafault), and stops before a specified numbers.

# range(start?, stop , step ? ) start = kha se shuru nkrna hai 2 stop = kha tk ye number include nhi hota
                               #step = kitne gap se badahna hai
# for i in range(50):
#     print(i)

# for i in range(2,40):
#     print(i)

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

# for i in range(0 , 101, -1):
#     print(i)

#print multification table of a number n.

#WAP to find the some of first n numbers.(using while)
# n = int(input("enter number: "))

# for i in range(1,10):
#     print(n*i)
    
# n = 5
# facto = 1
# i = 1
# while i <= n:
#     facto *= i
#     i += 1

# print("factorial =", facto)


#wap to find the factorial of first numbers.(using for)
#while loop

# n = 9
# sum = 0
# i = 0
# while i <= n:
#     sum += i
#     i += 1

# print("sum =", sum)

# this is a same process using a for loop
#for loop

# n = 4
# facto = 1
# for i in range(1, n+1):
#     facto *= i

# print("factorial =",facto)
    
# CALCULATOR DESIGN

# a = float(input("enter number: "))
# b = float(input("enter number: "))

# print("1. add ")
# print("2. subtract. ")
# print("3. multiply. ")
# print("4. divide. ")

# choice = float(input("enter choice: "))

# if choice == 1:
#     print("result =", a + b)
# elif choice == 2:
#     print("result =", a - b )
# elif choice == 3:
#     print("result =", a * b)
# elif choice == 4 :
#     print("result =", a / b)
# else:
#     print("invalid choice")
      



















