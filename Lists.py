item1="bread"
item2="milk"
item3="eggs"
item4="butter"
item5="cheese"
items=["bread","milk","eggs","butter","cheese"]                   
print(items)
print(items[0])
print(items[1])
print(items[2])
print(items[3])
print(items[4])

items[2]="cream"
print(items)

items.append("jam")
print(items)

items.remove("butter")
print(items)

items.pop(2)
print(items)

items.sort()
print(items)

items.reverse()
print(items)

items.insert(2,"butter")
print(items)

food=["bread","milk","eggs","butter","cheese"]
bathroom=["toothpaste","toothbrush","soap","shampoo","conditioner"]
bathroom.extend(food)
print(bathroom)

len(bathroom)
print(len(bathroom))

print("soap" in bathroom)