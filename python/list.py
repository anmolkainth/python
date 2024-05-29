marks=[5,7,9,"Anmol",True] #you can use multiple data types in a list
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1:4])#skips the item at 4th index
# print(marks[1:4:2])

# print(marks[-3]) #negative index
# print(marks[len(marks)-3]) #positive index


# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# if "Anmol" in marks:
#     print("Yes")
# else:
#     print("No")


# if "An" in "Anmol": #SAME GOES FOR STRINGS  
#     print("Yes")
# else:
#     print("No")


'''                               List comprehension                                '''

# lst=[i for i in range(5)]
# lst=[i*i for i in range(5)]
lst=[i for i in range(10) if i%2==0]
print(lst)