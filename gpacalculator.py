import csv
from collections import defaultdict
i=0
ci=0.0
gi=0.0
sgpa=0.0
b=[]
result=[]
name=""
l=0
F=0
a=defaultdict(list)
with open("3-2 results.csv",'r') as grades:
    for row in grades:
        for (k,v) in enumerate(row):
            a[k].append(v)
print(a[0])
i=0
for j in a[11]:
    if(j=='O'):
       b.append(10)
    if(j=='S'):
       b.append(9)
    if(j=='A'):
       b.append(8)
    if(j=='B'):
       b.append(7)
    if(j=='C'):
       b.append(6)
    if(j=='D'):
       b.append(5)
    if(j=='F'):
       b.append(0)
    i+=1

print(a[13])
for j in range(0,len(a[13])):
    a[13][j]=int(a[13][j])
    

n=int(input("Enter no.of students:"))
i=0
for j in range(0,n):
    for k in range(0,8):
        if(a[13][i]!=0):
            ci+=a[13][i]    
            gi+=a[13][i]*b[i]
            i+=1
        else:
            i+=1
            F+=1
    sgpa=gi/ci
    ci=0
    gi=0
    for k in range(0,10):
        name+=a[k][l]
    if(F!=0):
        print(name,"\t","Failed in ",F," Subjects\n\n")
    else:
        print(name,"\t",round(sgpa,2),"\n\n")
    name=""
    l+=8
    F=0
    



