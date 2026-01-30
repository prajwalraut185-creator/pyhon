#list slicing

mark = [90.9, 67.9, 90.8, 98.8, 78.0]
print(mark)
print(len(mark))
print(mark[3])
print(mark[4])

student = ["prajwal", 89.0, 18, "nagpur"]
print(student[3])
student[3] = "umred"
print(student)

mark = [64, 89, 98, 76 , 89, 90]
print(mark[-1:-3])

#list method

list = [1,3,4]
list.append(5)
print(list)

list = [9,7,6,4,5,3,1,2,8]
print(list.sort())        #assending
print(list)

list = [9,7,0,5,4,3,3,4,5,5]
print(list.sort(reverse=True)) #disassending
print(list)

list = [5,4,6,8,0,9,3,2,1,]
print(list.reverse())
print(list)

list = [1, 2, 4, 5, 6, 8,7]
list.insert(1,9)
print(list)

list = [3, 4, 5, 6]
list.remove(3)
print(list)

list = [7, 3, 5, 4]
list.pop(2)
print(list)