d={"tom":8439909231,"red":9219830013,"koke":8219893340}
d["jim"]=9302092313
print(d)
del d["koke"]
print(d)

for key in d:
    print("Key:",key,"Value:",d[key]) 

for k,v in d.items():
    print("Key:",k,"Value:",v)
d.clear()
print(d)
