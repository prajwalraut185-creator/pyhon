# CLASS OBJECT IN PYTHON

# class name:

#     name = "prajwal"

# c1 = name()
# print(c1.name)

# class car:
#     feature = "gesture"
#     price = "40000"

# c1 = car()
# print(c1.feature)
# print(c1.price)

# __INIT__ FUNCTION
# CONSTUCTER  # INITIALIZE MEAN = PRARAMBH KRNA
# self mtlb mai apne object ko naam de rha hu
# self.car ka mtlb jo object ke anda r naya print hone wala hai.

# Paramiterize constructor mean =  vo costructor jiske andar self ke 
# alava bhi kuch parameter hote hai

# class car:
    
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price

# c1 = car("bugadi","red", "price")
# print(c1.name, c1.color, c1.price, end= " ")


        # # default constructor 
# def __init__(self):
#     pass

# class & instance attributes
# attributes koi bhi data. ex.name, mark
# class.attr
# obj.at

# class student:
#     college = "ppr"
    
#     def __init__(self, name):
#         self.name = name

# c1 = student("prajwal")
# print(c1.name, c1.college )
                 
    
# MEAN
# class = design
# object = real cheez
# init = strating
# self = current object # present time obj
# method = action / behaviour

# class name:
    
#     college = "rbm"
    
#     def __init__(self, name,mark):
#         self.name = name
#         self.second = mark


# n1 = name("prajwal", 98)
# n2 = name("rahul", 87)

# print(n1.name,n1.college)
# print(n2.name, n2.college)




    
# practice question
# create student class that takes name & marks of 3 subject as argument 
# in consrtuctor. then create a method to print avgrage.

# class car:
    
#     def __init__(self, name, prize):
#         self.name = name
#         self.prize = prize

# c1 = car("rollce royal", "6cr")
# print(c1.name, c1.prize)


#     #    LOOP 

# class mark:
    
#     def get_avg(a,b,c,d,e,f):
#         avg = (a + b + c + e + f) / 5
#         print("average price", avg)

# mark.get_avg(12,34,5,6,7,89)
       
# abstraction mean = important cheez dikhana
# ex = key lagte ho start krte ho chalate ho = engine adar kaise kam
# kr rha hai ye muzhe hi pta its called abstraction

# class compitetion:
    
#     def race(self):
#         race_one = False
#         race_two = False
#         race_three = False
#         print("no start")
   
#     def race(self):
#         race_one = True
#         race_two = True
#         race_three = True
        # print("lets go start")


# c1 = compitetion()
# c1.race()

# class password:

#     def __init__(self, password):
#         self.password = password

#     def show_password(self):
#         print(self.password)

# p1 = password(935691)
# p1.show_password()

# create account class with 2 attributes - balance & account no.
# create method for debit.credit & printing thr balance

# class account:

#     def __init__(self, balance, account):
#         self.balance = balance
#         self.account = account

#     def debit(self,account):
#         self.balance -= account
#         print("rs", "balance", "aata ahe")
#         print("baki paise =", self.get_balance())

#     def credit(self, account):
#         self.balance += account
#         print("Rs", "balance", "aata ahe")
#         print("rs", "evdhe baki ahe =", self.get_balance())

#     def get_balance(self):
#         print(self.balance)

# a1 = account(1000,2000)
# a1.debit(100)
# a1.debit(200)
# a1.credit(400)
# a1.credit(900)

# OOPS APRT 2 
# DELETE KEYWORD
# USED TO DELETE OBJECT PROPERTIES OR OBJECT ISELF

# class student:
#     def __init__(self, mark):
#         self.mark = mark

# s1 = student(83)
# print(s1.mark)
# del s1.mark
# print(s1.mark)
             
# class password:
    
#     def __init__  private attribute and methods
# conceptual implementation in python
# private attributes & methods are meant to be used only within the
# calss and are not accessible from outside the calss
# PRIVTE __HO GAYI

# HM PRIVATE __DOUBLE UNDERSCORE SE KR SKTE HAI

# class ATM:

#     def __init__(self, pin, account):
#         self.pin = pin
#         self.account = account

#     def change__num(self):
#         print("pin:", self.pin)
#         print("account:", self.account)

# a1 = ATM(12321, 920004345689)
# print(a1.account)
# a1.change__num()


#                INHERITANCE 
# when one  class (child / derived) the propreties  & method of another 
# class (parent / base) base = jise properties li jaati hai
# yha propeties ka mtlb attr / method
# class car:
#   .....
# class toyoto car(car):
#   .....

# INHERUTANCE MTLB BINA LIKHE HI DUSRE CLSSS KA CODE USE KRNA.

# single inheritance 
# class python:
    
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def write():
#         print("program lihn suru kra....")
    
#     @staticmethod
#     def run():
#         print("program run kr....")
   
#     @staticmethod
#     def output():
#         print("aala re output............")

# p1 = python("java fullstack...")
# print(p1.name)
# p1.write()
# p1.run()
# p1.output()

# MULTY LEVEL INHERITANCE MTLB CLASS KE ANDRAR CLASS ADD KR SKTE HAI
# JAISE MAINE KIYE HAI

# class baba:
    
#     def bagh(self):
#         print("he property tuzhiz aahe")

# class porga(baba):
#     pass

# c1 = baba()
# c1.bagh()

# MULTIPLE INHERITANCE

# class val:
    
#     class a():
#         print("my name is prajwal")

#     class b():
#         print("i am working life")

#     class c(a,b):
#         print("i am  daily practice")

# c1 = val()
# c1.a()
# c1.b()
# c1.c()

# CLASS METHOD 
# a class method is bounfd to the class & recives the class as an 
# implict first argument

# note - staticmethod can't access or modify class state & generally 
# for utility.

#  CLASS METHOD ME CLASS ARGUMENT AATA HAI
#  INSTANCE METHOD ME SELF ARGUMENTNAATA HAI
# STATIC METOD NA OBJECT METHOD KA DATA USE KRTA HAI NA CLASS KA. 
#      class method #decorator
# class method class ko hi apne andar (class variable) ko use krta hai. selclass mark:

# class car:
    
#     class car():
#         pass
    
#     class car:
#         car = "bugadi"

#     @classmethod
#     def changecar(cls, car):
#         cls.car = car

# c1 = car()
# c1.changecar("fortuner")
# print(c1.car)
    
# @propety
# ham fuction ko bina ( ) ke ude kr skte ho
 
# class subject:

#     def __init__(self, a,b,c,d,e):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.e = e

#     @property
#     def percentage(self):
#         return str(int(self.a + self.b + self.c + self.d + self.e) / 5) + "%"

# s1 = subject(98,97,96,90,94)
# print(s1.percentage)

# s1.a = 90
# print(s1.percentage)


# polymophism mean = ek chij lkai rup me kaam # school me pdhata hai #ghjar me pita # dost me dost
# encpasulation = data ko chupa ke rjkhana aur use sidhe bdl nhi dena # atm machine 
# inheritance = ek calss dusre class ki guun le skti hai # sanskar
# abstraction = user ko jaruri chij dikhana baki undar ki process chupana
 
# polymorphism

# class sum:

#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(self.real, "a +", self.img, "b")

#     def __add__(self, num7):
#         newreal = self.real + num7.real
#         newimg = self.img + num7.img
#         return sum(newreal, newimg)
    
# sum1 = sum(90,130)
# sum1.shownumber()
# sum7 = sum(90,130)
# sum7.shownumber()

# result = sum1 + sum7
# result.shownumber()



