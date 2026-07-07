class Human:
    def __init__(self,n,g,a,w):
        self.name=n
        self.gender=g
        self.age=a
        self.work=w
    def info(self):
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Age:",self.age)
        print("Work:",self.work)

    def do_work(self):
        print(self.name,"is doing/playing",self.work)
    def do_info(self):
        print("Name:"+self.name+"\nGender:"+self.gender+"\nAge:"+str(self.age)+"\nWork:"+self.work)