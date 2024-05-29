# import random
# num= random.randint(1,20)
# counter=0
# while counter<5:
#     guess=int(input("Choose a number between 1-20:"))
#     if guess==num:
#         print("You win")
#         break
#     else:
#         counter+=1
# if counter==5:
#     print("You lose.\nThe number was:",num)


# for i in range(1,8):
    # for j in range(1,i):
        # print("*", end=' ')
    # print()


# str=input("Enter a string:")
# a=len(str)
# i=0
# for j in range (-1,(-a-1),-1):
#     print(str[i],"\t",str[j])
#     i+=1



# n=int(input("Enter a number:"))
# s = str(n)
# if '2' in s:
#     print("Yes")
# else:
#     print("No")



string="*"
pattern=''
r=int(input("How many rows do you want:"))
for a in range(r):
    pattern+=string
    print(pattern)