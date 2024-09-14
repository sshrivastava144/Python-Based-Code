# write a program to count the word'''

str1=input('enter the string')
final_str1=''
i=0
while(i<=len(str1)-1):
    
    if (str1[i]!=' '):
        final_str1=final_str1+str1[i]
        i=i+1
    else:
        i=i-1
print(final_str1)