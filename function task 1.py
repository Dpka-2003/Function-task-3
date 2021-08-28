def most_frequent(a):
        d={}
        for i in a:
            b=a.count(i)
            d[i]=b
        return d
string=input("Enter a string: ")
n=most_frequent(string)
f=sorted(n.items(),key=lambda x:x[1],reverse=True)
for i in f:
    print("%s=%02d"%(i[0],i[1]))
