expenses=[6900,6090,9600,6009,9006,9060]
total=0
for expense in expenses:
    total+=expense
print(total)

for i in range(1,11):
    print(i)

for i in range(len(expenses)):
    print('Month:',i+1,'Expense:',expenses[i])
    total+=expenses[i]
print('Total Expense:',total)

key_locations="chair"
locations=["bedroom","kitchen","study","chair","guest room"]
for location in locations:
    if location==key_locations:
        print("Key found in ",location)
        break
    else:
        print("Key not found in",location)


for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)

i=1
while i<=10:
    print(i)
    i+=1