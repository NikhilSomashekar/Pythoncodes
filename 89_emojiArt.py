#Without string multiplication(Nested loop)
#---------------------------
# for x in range(10):
#     i=1
#     while i<=x:
#         print("*",end = ' ')
#         i +=1
#     print("")
#---------------------------
#Using for 
#---------------------------
# for num in range(10):
#     print("*"*num)
#---------------------------
#Using while
#---------------------------
# num = 1
# while num<10:
#     print("*"*num)
#     num += 1
#---------------------------
# 
space = 9
for num in range(10):
    print(" "*space," #"*num)
    space -= 1
    #print()

