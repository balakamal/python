import csv
from collections import defaultdict
i=0
fi=""
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
        for v in row:
            if(v=="\n"):
                a[i].append(fi)
                i=0
                fi=""
            elif(v==","):
                a[i].append(fi)
                i+=1
                fi=""
            else:
                fi+=v
        fi=""
for j in a[1]:
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

for j in range(0,len(a[2])):
    a[2][j]=int(a[2][j])
    

n=int(input("Enter no.of students:"))
s=int(input("Enter no.of subjects:"))
i=0
for j in range(0,n):
    for k in range(0,s):
        if(a[2][i]!=0):
            ci+=a[2][i]    
            gi+=a[2][i]*b[i]
            i+=1
        else:
            i+=1
            F+=1
    sgpa=gi/ci
    ci=0
    gi=0
    if(F!=0):
        print(a[0][l],"\t","Failed in ",F," Subjects\n\n")
    else:
        print(a[0][l],"\t",round(sgpa,2),"\n\n")
    l+=s
    F=0
