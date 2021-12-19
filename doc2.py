n1=int(input("enter the no."))
n2=int(input("enetr the no"))
n3=int(input("enetr the no"))
if n1>n2 and n1>n3:
    print(n1,"greater")
elif n2>n1 and n2>n3:
    print(n2,"greater")
elif n3>n1 and n3>n2:
    print(n3,"greater")
else:
    print("equal")