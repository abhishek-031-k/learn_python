'''
a = "a very long string with emails"
# '''
# # this code is for reading
# f = open("file.txt", "r")
# data = f.read()
# print(data)
# f.close()

# this code is for write in the file

# str = "you got placed before midsem"
# f = open("file.txt", "a")
# f.write(str)
# f.close()


# you dont have to close the file
with open("file.txt") as f:
    print(f.read())