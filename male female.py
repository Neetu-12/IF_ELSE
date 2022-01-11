gender=input("enter the gender:-")
age=int(input("enter the age:-"))
if gender=="male":
    if age>18:
        print("he will earn 20,000")
    else:
        print("he can't do work")
elif gender=="female":
    if age>18:
        print("she will earn 15,000")
    else:
        print("she can't do work")