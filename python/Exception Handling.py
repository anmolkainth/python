# ValueError, IndexError 

# a=input("Enter a number: ")
# print(f"Multiplication table of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# # except Exception as e:
# #     print(e)#prints the error
# except:
#     print("Invalid input")

# print("End of program")


# try:
#     num = int(input("Enter an index(0 or 1): "))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("Number is not an integer.")
# except IndexError:
#     print("Index Error")


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:#it is used with functions(always gets executed)
    print("I am always executed") #will print
  
  # print("I am always executed") #will not print  


x = func1()
print(x)