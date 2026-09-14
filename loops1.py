# # # # i = 0
# # # # while(i < 8):
# # # #     print(i)
# # # #     i += 1             

# # # l = [1, "abhishek", False, "print"]
# # # i = 0
# # # while i < len(l):
# # #     print(l[i])
# # #     i += 1 

# # l = [1, 2, 3, 4, 5, 6, 7, 8]
# # for i in l:
# #     print(i)
# l = [1, 2, 3]
# for item in l:
#     print(item)
# else:
#     print("done")    

n = int(input("Enter a number: "))

# while(i < 11):
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# sum = 0
# while(i <= n):
#     sum += i
#     i += 1
# print("Sum of first n natural number is: ",sum)    

# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(f"factorial of {n} is: {fact}")

# for i in range(1,n+1):
#     print(" "*(n-i), end = "")
#     print("*"*(2*i-1))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end = "")
#     print("")    

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*"* n)
    else:
        print("*", end = "")
        print(" "*(n-2), end = "")
        print("*")    