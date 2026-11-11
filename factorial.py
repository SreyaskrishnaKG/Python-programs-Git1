# pgm to print the factorial number

num=int(input("enter a number ::"))
temp=1
for i in range(1,num+1):
    temp *=i
print(temp)