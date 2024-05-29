# for i in range (5):
#     print(i)
# else:
#     print("Sorry no i")

'''will the else statement print or not
Hence, 'else' doesn't break the loop'''
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i")  