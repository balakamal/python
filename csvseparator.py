import csv
from collections import defaultdict
i=0
fi=""
a=defaultdict(list)
fname=input("Enter filename:")
with open(fname,'r') as grades:
    for row in grades:
        for v in row:
            if(v=="\n"):
                a[i].append(fi)
                i=0
                fi=""
            elif(v=="," and "\"" not in fi):
                a[i].append(fi)
                i+=1
                fi=""
            else:
                fi+=v
        fi=""
print(a)
