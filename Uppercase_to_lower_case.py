# write a program to convert all the character in astring to upper case to lower case

inputstr=input('enter the word')
final_str=''
for i in inputstr:
    data=i
    asciivalue= ord(data)
    if (asciivalue>=65 and asciivalue<=90):
        final_str=final_str+data
    else:
        asciivalue=asciivalue+32
        data=chr(asciivalue)
        final_str=final_str+data
print(final_str)
