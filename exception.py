X=input("Enter a number1 : ")
Y=input("Enter a number2 : ")
try:
    Z=int(X)/int(Y)
except Exception as e:
    print("Exception : ",e)
    Z=None
print("DIvision is : ",Z)

