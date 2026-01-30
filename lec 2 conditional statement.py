light = "pink"

if(light == "red"): #if = agar
    print("stop")
elif(light == "green"): #elif = warna agar 
    print("go")
elif(light == "yellow"): #
    print("look")
else:
    print("broken") #else = warna


age  = 12

if(age >= 18 ):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can vote")

else:
    print("cannot vote")

mark = int(input("enter student mark: "))

if(mark >= 90):
    grade = "topper"
elif(mark >= 80 and mark <= 90):
    grade = "intelligent"
elif(mark >= 70 and mark <= 80):
    grade = "average"
elif(mark >= 50 and mark <= 70):
    grade = "better"
elif(mark >= 40 and mark <= 50 ):
    garde = "poor"
elif(mark >= 35 and mark <= 40):
    grade = "very poor"
else:
    grade = "fail"

print("student of the mark ->", grade)




    




