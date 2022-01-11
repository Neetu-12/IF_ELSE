a=int(input("enter the no"))
if a%4==0:
    print("leap year")
else:
    print("not leap year")


# a=int(input("enter the no:-"))
# if a%100==0:
#     print("leap yrrrr...")
# else:
#     if a%4==0:
#         print("leap year")
#     else:
#         print("not leap year")


###NESTED IF ELSE:----
yr=int(input("enter leap year :-"))
if yr%100==0:
	if yr%400==0:
		print("leap year")
	else:
		print("not leap yr")
else:
	if yr%4==0:
		print("leap year")
	else:
		print("not a leap year")
