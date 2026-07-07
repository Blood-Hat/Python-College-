num=input("Enter a number:")
num=int(num)
if num>0:
    print("Number is positive")
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")
elif num==0:
    print("Number is zero")
else:
    print("Number is negative")
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")



indian=["samosa","pav bhaji","chana masala"]
chinese=["noodles","dumplings","egg rolls"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish:")
if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("Italian")
else:
    print("International")



