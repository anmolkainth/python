# def average(a=6,b=2):
#     print("Average is: ",(a+b)/2)

# average()
# average(5)#only changes the value of a
# average(b=10)#changes the default value of b 


# def name(f_name,mid_name="Singh",last_name="Parhar"):
#     print("Hello",f_name,mid_name,last_name)


# name(last_name="Kainth",f_name="Anmol",mid_name="") #Keyword arguments


# a=input("Enter your first name: ")
# name(a)


'''                     Variable Length Argument                             '''

# def average(*numbers): # '*' means variable/converts into tuple
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     avg=sum/len(numbers)
#     #print("Average is: ", avg)
#     return avg

# c=average(2,5,8,7)
# print(c)

def name(**name):
    print(type(name))
    print("Hello",name["f_name"],name["m_name"],name["l_name"])

name(m_name="Buchaan",l_name="Barnes",f_name="James")