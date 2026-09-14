# def greeting():
#     print("Good Morning")

# greeting()    

# def goodDay(name):
#     print("Good Morning, " + name)
#     return "done"

# a = goodDay("abhishek")    
# print(a)


# def goodDay(name, ending = "thank you"):
#     print("Good Morning, " + name)
#     print(ending)
   

# goodDay("abhishek")    
# goodDay("akmax", "thanks")


def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))

print(f"Factorial of n is: {factorial(n)}")