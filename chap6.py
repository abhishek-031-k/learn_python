marks1 = int(input("enter marks1: "))
marks2 = int(input("enter marks2: "))
marks3 = int(input("enter marks3: "))

total_marks = marks1 + marks2 + marks3
if(total_marks >= 120):
    if(marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
        print("passed")
    else:
        print("failed due to less than 33% marks in a subjets")

else:
    print("got less than 40% in total")            