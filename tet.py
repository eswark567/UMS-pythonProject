class uniq:
    def __init__(self,p):
        self.p=p

    def uniqcount(self):
        k=[]
        count=0
        for i in self.p:
            if i not in k:
                k.append(i)
        for j in k:
            count=0
            for i in self.p:
                if j==i:
                    count=count+1
            print("value is:",j,"with","count",count)

obj=uniq(p=[1,1,1,1,2,2,2,2,2,2,3,3,6,6,6,6,6,6,6,4])
obj.uniqcount() 