# write a prgram to 5 reverse word
num1='shivam shrivastava'
kk=''
number=0
for i in num1:
    if number<6:
        kk=i+kk
        number=number+1
    else:
        kk=kk+i
print(kk)