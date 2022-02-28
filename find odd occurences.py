#program to find odd occurences in a given list
x=[1,2,3,2,1,3,2,1,2,2,4,5,6,6,4,5,2,3,1]
l=[]
for i in x:
    if i not in l:
        p=x.count(i)
        if p%2==1:
            l.append(i)
print(l)
output:
[3]
