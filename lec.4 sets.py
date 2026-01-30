collection = {1, 2, 3, 4, "hello", "world"}

print(collection)
print(type(collection))
print(len(collection))


collection = set()

print(type(collection))

#sets method
collection.add(45)
collection.add(12)
collection.add(12)

collection.remove(45)

print(collection)

collection.add(67)
collection.add(87)
collection.add(98)

collection.clear()
print(len(collection))

collection = {"event", "student", "percentage", "productivity"}

print(collection.pop())
print(collection.pop())
print(collection.pop())


set1 = {1, 2, 3, 4}
set2 = {1, 6, 4, 5}

print(set1.union(set2))
print(set1)
print(set2)

set1 = {1, 9, 3, 6}
set2 = {7, 9, 5, 6}

print(set1.intersection(set2))

#lets practice 
#store following word meaning in a python dictionary:
     #table: "a piece of furniture", "list of fact & figures"
     #cat : "a small animal"

dict = {
    "table" : "a piece of furniture", "list of fact & figure"
    "cat" : "a small animal"


}
print(dict)

#1.you are given a list of subject for student. assume one classroom is required for 1 
#1.suject.how many classroom are needed by all students.

#"python", "java", "c++", "python", "javascript", "java", "c++", "c"

subjects = {
    "python", "java", "c++", "python", "javascript", "java", 
    "c++", "c", "java",
}

print(subjects)
print(len(subjects))

#WAP to enter marks of  3 subject from the user and store them in a dictionary. start with abd emty
#dictionary & add one by one. use subject name as key & mark as value

percentage = {}

x = int(input("enter phy: "))
percentage.update({"phy" : x})
x = int(input("chem: "))
percentage.update({"chem" : x})

#figure out a way to store 9 & 9.0 as separate values in the set.
#you can take help of built-in data type

values = {
    ("float" , "90.6"),
    ("int" , "90"),
    ("string" , "animal"),
   ("boolean" , "True") 
}

print(values)