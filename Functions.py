def calculate_expenses(exp_list):
    total=0
    for expense in exp_list:
        total+=expense
    return total

tom_exp_list=[2100,3400,5600,8700]
jerry_exp_list=[1200,2300,3400,4500]
tom_total=calculate_expenses(tom_exp_list)
jerry_total=calculate_expenses(jerry_exp_list)
print("Tom's total expenses:",tom_total)
print("Jerry's total expenses:",jerry_total)

if tom_total>jerry_total:
    print("Tom spent more money than Jerry")
elif tom_total<jerry_total:
    print("Jerry spent more money than Tom")
else:
    print("Tom and Jerry spent the same amount of money")


def sum(a,b=0):
    print("a:",a)
    print("b:",b)
    sum=a+b
    print("Total inside function:",sum)
    return sum
n=sum(5,6)
print("Total outside function:",n)

