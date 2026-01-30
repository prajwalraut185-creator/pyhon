info = {
    "key" : "value",
    "name" : "prajwal",
    "learning" : "apna college",
    "answer" : False,
    "dream" : "coder",
    "action" : "ptyhon",
    "list" : ["pyhton", "java", "java script", "c", "c++"],
    "loops" : ("dictionary","set"),
    12 : 90.9

}
print(type(info))

#muatable

info = {
    "name" : "prajwal",
    "college" : "apna college",
    "study" : "pyhton programming",
    "goal" : "coder",
    "happy" : "coading",

}

info["name"] = "hai"
print(info)

#Nested dictionary
college = {
    "subject" : "account",
    "college" : "sem mark",
    "mark" :{
        "first sem" : 89,
        "second sem" : 99,
        "third sem"  : 98,
    }
}
print(college["mark"]["second sem"])

#dictionary method
mark = {
    "student" : "first sem",
    "first student" : "second sem",
    "second student" : "third sem",
    "third student" : "final year",

}

print(len(mark))
print(mark.keys())

mark = {
    "entry" : "final account",
    "transction" : "jounral entry",
    "particulors" : "ammount",

}

print(mark.values())
print(list(mark))

mark = {
   "student" : "topper",
   "second"  : "avg",
   "third" : "poor",

}

pairs = list(mark.values())
print(pairs[0])

mark = {
    "first topper" : 98,
    "second topper" : 97.99,
    "third topper" : 97.98

}

print(mark.get("third topper"))

mark = {
    "first percentage" : 90,
    "second percentage" : 98,
    "third percentage" : 99

}
new_dict = {"third percentage" : "91"}
mark.update(new_dict)
print(mark)
