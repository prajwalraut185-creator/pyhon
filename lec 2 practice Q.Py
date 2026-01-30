a = int(input("enter first number: "))
b = int(input("enter  second number: "))
c = int(input("entr third number: "))
d = int(input("ente fourth number: "))
e = int(input("netr fifth number: "))


if( a >= b and a >= c and a >= d and a >= e):
    print("first number is largest", a)
elif(b >= c and b >= d and b >= e):
    print("second numberis largest", b)
elif(c >= d and c >= e):
    print("third numnber is largest", c)
elif(d >= e):
    print("fourth number is largest", e)
else:
    print("fifth numnber is largest")

num = int(input("enter the number: "))


if(num % 2 == 0):
    print("even")
else:
    print("odd")


num = int(input("enter the number: "))


rem = num % 32
if(rem == 0):
    print("multiple of 7")
else:
    print("not a multiple 7")











