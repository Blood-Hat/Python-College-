def cal_area(base, height):
    return 0.5 * base * height

if __name__=="__main__":
    print("I am in area.py")
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area: ", cal_area(base, height))
else:
    print("Module imported successfully")
