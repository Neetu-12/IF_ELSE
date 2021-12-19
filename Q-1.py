# a=2
# b=3
# c=4
# d=5
# if a>b:
#     print("a is greater than b")
#     if c>d:
#         print("c is greater than d")
#     else:
#         print("c is greater")
# else:
#     print("d is greater than c")

age=int(input("enetr age"))
gender=input("Enter your gender")
if age>=18:
    if gender=="male":
        print("A licence")
    elif gender=="female":
        print("B licence")
else:
    print("Not allow licence")