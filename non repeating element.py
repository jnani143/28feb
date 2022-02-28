#program to find out non repeating element in a given list
x=[1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 34, 6, 3, 2, 1, 4, 5, 6, 8, 9, 90, 8, 8, 57, 1, 2]
l=[]
for i in x:
    if i not in l:
        p=x.count(i)
        if p==1:
            l.append(i)
print(l)
output:
[34, 9, 90, 57]
