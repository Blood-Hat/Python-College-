f=open("E:\\data\\funny.txt","w")
f.write("Python is best")
f.close()
f=open("E:\\data\\funny.txt","r")
print(f.read()) 
f.close()

f=open("E:\\data\\funny.txt","a")
f.write("\nJava is better than Python")
f.close()
f=open("E:\\data\\funny.txt","r")
print(f.read()) 
f.close()

f=open("E:\\data\\fun.txt","w")
f.write("Teacher:Why are you late, Frank\nFrank:Because the traffic sign\nTeacher:What traffic sign?\nFrank:The one that says'School Ahead, Go Slow'")
f.close()
f=open("E:\\data\\fun.txt","r")
print(f.read())
f.close()

f=open("E:\\data\\fun.txt","r")
for line in f:
    line=line.strip()
    words=line.split(' ')
    print(words)
f.close()

f=open("E:\\data\\fun.txt","r")
f_out=open("E:\\data\\fun_out.txt","w")
for line in f:
    words=line.split(' ')
    f_out.write(line+" WordCount: "+str(len(words)) +"\n")
f.close()
f_out.close()

f_out=open("E:\\data\\fun_out.txt","r")
print(f_out.read())
f_out.close()

with open("E:\\data\\fun.txt","r") as f:
    print(f.read())
print(f.closed)