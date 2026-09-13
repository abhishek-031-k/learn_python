a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3 "))
d = int(input("Enter number4: "))

# if(a >= 18):
#     print("you are an adult")

# else:
#     print("you are a child")        

# print("End of program")    

if(a > b and a > c and a > d):
    print("greatest number is ", a)
elif(b > a and b > c and b > d):
    print("greatest number is ", b)
elif(c > a and c > b and c > d):
    print("greatest number is ", c)
else:
    print("greatest number is ", d)    