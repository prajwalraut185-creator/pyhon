#slicing tuple

tup = (9, 7, 6, 5, 3)
print(tup[1])
print(tup)

tup = ()
print(tup)
print(type[tup])

tup = (3, 4, 5, 6, 7,)
print(tup[1:4])

tup = (3, 4, 6, 7, 9,)
print(tup[:3])

tup = (4, 5, 9, 4, 3)
print(tup[3:])

#tuple method

tup = (2, 4, 5, 6, 9)
print(tup.index(9))

tup = (9, 9, 9, 7, 7, 5 )
print(tup.count(5))

#practice question
#WAP to ask the user to enter names of their 3 favourate shows $ store them a list

show = []
show.append(input("enter first show: "))
show.append(input("enter second show: "))
show.append(input("enter third show: "))

print(show)

#WAP to check if a list contains a palindrome of element.(Hint:use copy()method)
  #[1,2,3,3,2,1]             [1,"abc", "abc, 1]

list1 = [2,3,4]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palidrome")
else:
    print("not palidrome")

#WAP to count the number of student with the "a" grade in the following tuple
            # ["c", "d", "a", "a", "b", "b", "a"]
    
grade = ("C", "D", "A", "A", "B", "B", "b")
print(grade.count("A"))

#store the above vlaue in list & sort then from "a" to "b".

list = ("addocate", "addition", "attractive", "appoinment", "ajustment", "anything", "everything")
print(list.sort())
print(list)






