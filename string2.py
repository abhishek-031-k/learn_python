# name = input("Enter your name: ")

# print(f"Good afternoon {name} ")

name = input("enter your name: ")

string1 = '''Dear <|{name}|>,
you are selected!
<|{date}|>
      '''

print(string1.replace("<|{name}|>", "abhishek").replace("<|{date}|>", "11 sept"))

s = "my name is abhishek  "
print(s.find("  "))
print(s.replace("  ", " "))