water=int(input("enter the liter"))
if water<=1:
    print("need to be filled")
elif water>1 and water<10:
    print("no need to fill")
else:
    print("overflow")
