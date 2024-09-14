# write a program to take 5 integer in a list and display only the even numbers

l=[78,323,23,4,46,35,22]
l1=[]
for i in l:
    if i %2==0:
        l1.append(i)
print(l1)