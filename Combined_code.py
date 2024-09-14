#<<<<<<<<<python   code>>>>>>>>>>>>>



# write a program to check a aplindrome or not a palindroe
'''n=int(input("enter the number"))
f=n
rev=0
while n>0:
    rev=(rev*10)+n%10
    n=n//10
if rev==f:
    print(rev,"is a palindrome")
else:
    print(rev,"is not a palindrome number")'''

# ----------------------------------------------------------------------------------

# write a program to reverse word&sentence

'''str1='SHIVAM SHRIVASTAVA'
rev_str1=""
for i in str1:
    # print(i)
    rev_str1=i+rev_str1
print(rev_str1)'''

# airthmatic operation  +/*

'''str1='shivam'
str2='shrivastava'
str2_final_value=str1+str2
print(str2_final_value)
print(str2_final_value*5)'''

# string comparison

'''str1='shivam'
str2='shivam'
if str1==str2:
    print('str1 is eual to str2')
else:

    print('str1 is not equal to str2')'''


'''str1='shivaM'
str2='shivam'
if str1==str2:
    print('str1 is eual to str2')
else:

    print('str1 is not equal to str2')'''

'''str1='shivaM'
str2='shivam'
if str1>str2:
    print('str1 is eual to str2')
else:

    print('str1 is not equal ')'''


'''str1='shivaM'
str2='shivam'
if str1<str2:
    print('str1 is eual to str2')
else:

    print('str1 is not equal ')'''


# ----------------------------------------------------------

# string methods
# upper method
'''str1='shivamshrivastava'
str2=str1.upper()
print(str2)'''

# lower method

'''str1='shivam shrivastava'
str2=str1.lower()
print(str2)'''

# swapcase() method

'''str1='ShivAmshRiVAstava'
str2=str1.swapcase()
print(str2)'''

# write a program to convert all the character in a string to lower case without using lower
'''inputstr=input('enter the word')
final_str=''
i=0
while(i<=len(inputstr)-1):
    data=inputstr[i]
    ascivalue=ord(data)
    if (ascivalue>=97 and ascivalue<=122):
        final_str=final_str+inputstr[i]
        i=i+1
    else:
        ascivalue=ascivalue+32
        data=chr(ascivalue)
        final_str=final_str+data
        i=i+1
print(final_str)'''

# write a program to convert all the character in astring to upper case to lower case

'''inputstr=input('enter the word')
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
print(final_str)'''

# count the word
'''str1='shivam shrivastava'
count1=0
for i in str1:
    count1=count1+1
print(count1)'''

# write the program to count of character
'''str1='shivamshrivastava'
dict1={}
count1=0
for i in str1:
    print('shivam shrivastava')'''

# ---------------------------------------------------------------------------------
# replace method
'''str1="where are you"
str2=str1.replace("are","was")
print(str2)'''
# -----------------------------------------------
# count method
'''str1="where are you"
num=str1.count('are')
print(num)'''

# --------------------------------------------------
# startswith() method
'''str1="where are you"
if (str1.startswith("where")):
    print("start with where")
else:
    print('not start with where')'''

# -------------------------------------------------------------
# endswith

'''str1='where are you'
if (str1.endswith('your')):
    print('end with')
else:
    print('without ends')'''
# ------------------------------------------------------------------
# in operator
# ------------------------------------------------------------
# find()/rfind()
'''str1='when the going gets tough only the tough gets going'
print(str1.find('tough'))
print(str1.rfind('tough'))'''
# ------------------------------------------------------------------
# index/rindex
'''str1='when the going gets tough only the tough gets going'
print(str1.index('tough'))
print(str1.rindex("tough"))'''
# ---------------------------------------------------------------

# isalpha()/isdigit/isnum
# str1="whenthegoinggetstoughonly"
# if (str1.isalpha()):
#     print("shivam")


# digit1='123124343'
# if(digit1.isdigit()):
#     print('daclsdhach')

# num1_al='237498jjkdacfkvchf'
# if (num1_al.isalnum()):
#     print('dchsdoch')

# str1='shivam'
# if(str1.isalpha()):
#     print('true')

# ------------------------------------------------------


# -------------------------------------------------------



# write a progranm to remova all whitespaces
'''str1=input('enter the word & sentence')
new_str1=''
for j in str1:
    if j!=' ':
        new_str1=new_str1+j
print(new_str1)


# write a program to count the word'''

'''str1=input('enter the string')
final_str1=''
i=0
while(i<=len(str1)-1):
    
    if (str1[i]!=' '):
        final_str1=final_str1+str1[i]
        i=i+1
    else:
        i=i-1
print(final_str1)'''
# -----------------------------------------------------------------------------
# write a program to count a word
'''str1='shivam shrivastava'
count1=0
for i in str1:
    # print(i)
    count1=count1+1
print(count1)'''


# --------------------------------------------------------------------------------
# write a prgram to 5 reverse word
'''num1='shivam shrivastava'
kk=''
number=0
for i in num1:
    if number<6:
        kk=i+kk
        number=number+1
    else:
        kk=kk+i
print(kk)'''

'''str1='shivamshrivastava'
str2=''
for i in str1:
    # print(i)
    if i not in str2:
        str2=str2+i
print(str2)'''

'''str1='shivam'
str2=''
kk=str1[1]
print(kk)'''

# write a program the replace a value without using any method

'''str1='shivam'
str2=''
for i in str1:
    if i!='s':
        str2=str2+i
    else:
        str2=str2+'l'
print(str2)
'''
# -----------------------------------------------------------------------

# string formatting
'''name=(input('enter the name'))
age=input('enter the age')
marks=input('enter the marks')
print(name,'of age',age,'has scored',marks,'marks')
print('{}of age{}has scored{}marks'.format(name,age,marks))
# print("marks={}/nage={}/nname={}".format(name,marks,age))---------------------positional parameter'''
# ----------------------------------------------------------------------------------------------

# write a progarm to swap value
'''x=50
y=60
z=x
x=y
y=z
print(x,y)'''


# parameter passing techniques

# formal v/s actual parameter
''''class demo:
    def _init_(self):
        self.h=999
        self.i=777
    def swap(self,x,y):
        temp=x
        x=y
        y=temp
d1=demo()
a=10
b=20
d1.swap(a,b)'''

# -----------------------------------------------------------------




'''class calculator:
    def disp(self,a=999,b=777,c=666):
        print(a)
        print(b)
        print(c)
c1=calculator()
x,y,z=10,20,30
c1.disp(x,y,z)
c1.disp(x,y)
c1.disp(x,y)
c1.disp(x)'''


# ------------------------------------------------------------------------------------------
'''class display:
    def disp(self,name='NA',age=0,marks=0):
        print(name)
        print(age)
        print(marks)
d1=display()
n,a,m='shivam',19,75
d1.disp(marks=m)
d1.disp(age=a,name=n)'''
# --------------------------------------------------------------------------------------------
# write a program to find the discount number

'''discount=int(input('enter the discount'))
sp=int(input('enter the selling price'))
kk=(discount/sp)*100
discount=sp-kk
print(discount)'''

# ----------------------------------------------------------------------

'''
class calculator:
    def calc(self,a,b):
        res1=a+b
        res2=a-b
        res3=a*b
        res4=a/b
        return res1,res2,res3,res4
c1=calculator
x,y=10,20
x1,x2,x3,x4=c1.calc()
print(x1)
print(x2)
print(x3)
print(x4)
'''
# ---------------------------------------------------------------------------
'''
class calculator:
    def _add_(self,*values):
        i,sum=0,0
        while(i<=len(values)-1):
            sum=sum+values[i]
            i=i+1

        print(sum)
c1=calculator()
c1._add_(10,20)
c1._add_(10,20,39)
c1._add_(10,20,393,45)'''

# -------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------


# write a program to  string  number

'''kk='shivam shrivastav'
str1=''
for i in kk:
    str1=i+str1
print(str1)'''

'''list1=[12,345,64,34,21,76,78]
max1=list1[0]
for i in list1:
    if i<max1:
        i=max1
print(max1)'''


# Python program to capitalize the first and last character of each word in a string

'''String = input('Enter the String :')

String = String[0:1].upper() + String[1:len(String)-1] + String[len(String)-1:len(String)].upper()
print(String)'''


# python program to check if a string has at least one letter and one number

'''str1='shivam12'
print(type(str1))'''

# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4

'''str1='abcdef'
str2='defghia'
count1=0
for i in str1:
    for j in str2:
        if i ==j:
            count1=count1+1
print(count1)'''

# Python – Uppercase Half String
# str1='shivam'
# str3=len(str1)
# # str2=len(str1)
# str2=str1[len(str1)-1:len(str1)].upper()
# print(str2)

# ---------------------------------------------------------------
# global variable
# -----------------------------------------------------------------------------

# lambda function

# write a program to take 5 integer in a list and display only the even numbers

'''l=[78,323,23,4,46,35,22]
l1=[]
for i in l:
    if i %2==0:
        l1.append(i)
print(l1)'''

'''l=[]
l1=[]
i=0
while i<=4:
    num=int(input('enter the number'))
    l.insert(i,num)
    i=i+1
# print(l)
for i in l:
    if i%2==0:
        l1.append(i)
print(l1)'''

# without append() method
'''l=[]
i=0
while i<=4:
    num=int(input('enter the number'))
    l.insert(i,num)
    i=i+1
def even(x):
    if x%2==0:
        return 1
    else:
        return 0
i=0
while (i<=4):
    status=even(l[i])
    if (status==1):
        print(l[i],end=' ')
    i=i+1'''



'''ptr1=lambda x,y :x+y
ptr2=lambda num:num*num
res1=ptr1(10,20)
res2=ptr2(6)
print(res1)
print(res2)'''


# --------------------------------------------------------------------

# ;;;;ldef even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[]
# i=0
# while (i<=4):
#     num=int(input('enter the number'))
#     l.insert(i,num)
#     i=i+1
# p=list(filter(even,l))
# print(p)


# ------------------------------------------------------------------
'''l=[]
i=0
while (i<=4):
    num=int(input('enter the numeber'))
    l.insert(i,num)
    i=i+1
p=list(filter(lambda x :x%2==0,l))
print(p)'''

# ------------------------------------------------------------------------------



# write a program to print facrroial number
# n=int(input('enter the any number'))

# step1 :
# '''55|Webbrowsing|Facebook|3
# 56|Webbrowsing|Whatsapp|4
# 57|Webbrowsing|tinder|6
# 58|Webbrowsing|Fauji|11
# 59|Webbrowsing|Twitter|8
# 60|Webbrowsing|Instagram|2
# 551|Game|Carem|4
# 561|Game|Ludo|7
# 571|Game|Cricket|6
# 581|Game|Fauji|11
# 591|Game|8poll|8
# 601|Game|fotball|2'''
#
'''fo = open('C:\\Users\\gj\\Downloads\\data (1).txt', 'r')
data = fo.readlines()
list1 = []
for i in data:
    kk = i.replace('\n', '')
    list1.append(kk)
del list1[0]
str1 = ''
list3 = []
for i in list1:
    list2 = i.split("|")
    del list2[0]
    res1 = "|".join(list2)
    list3.append(res1)
dict1 = {}
set1 = set(list3)
for i in list3:
    dict1[i] = list3.count(i)
print(dict1)'''

# ----------------------------------------------------------
# nested function

'''def outerfunction():
    a=99
    def innerfunction():
        b=20
        print(a)==============================================>>>will beerror
        print(b)
    innerfunction()
    print(a)
    print(b)
outerfunction()'''

# -------------------------------------------------------------

'''a=999
def outer():
    a=99
    b=gu
    def inner():
        a=99
        b=20
        c=30
        print(a)
        print(b)
        print(c)
    inner()
    print(a)
    print(b)
outer()
print(a)'''

# --------------------

'''a=99
def outer():
    global a
    a=99
    b=200
    def inner():
        global a
        a=9
        nonlocal b
        b=20
        c=30
        print(a)
        print(b)
        print(c)
    inner()
    print(a)
    print(b) 
outer()
print(a)'''
# --------------------------------------------------------------------------------

# modules
# list1=[12,43,65,353,435,43]
# max1=list1[0]
# for i in list1:
#     if


# --------------------------------------------------------

# write a program to print facrroial number
# n=int(input('enter the any number'))

# step1 :
# '''55|Webbrowsing|Facebook|3
# 56|Webbrowsing|Whatsapp|4
# 57|Webbrowsing|tinder|6
# 58|Webbrowsing|Fauji|11
# 59|Webbrowsing|Twitter|8
# 60|Webbrowsing|Instagram|2
# 551|Game|Carem|4
# 561|Game|Ludo|7
# 571|Game|Cricket|6
# 581|Game|Fauji|11
# 591|Game|8poll|8
# 601|Game|fotball|2'''
#
# fo = open('C:\\Users\\gj\\Downloads\\data (1).txt', 'r')
# data = fo.readlines()
# list1 = []
# for i in data:
#     print(i[])

# /


# -----------------------------------------------------------------------

'''n=int(input('enter the number'))
if n%2==0:
    print('sum')
else:
    print('odd')'''

# -----------------------------------------

'''list1=[76,23,4,34,43,4,24,234,23,324]
max1=list1[0]
for i in list1:
    # print(i)
    if i>max1:
        max1=i
print(max1)'''

# Q3. Write a Python program to divide them into three groups, Based on the users age. Group 1 : Age <18
# , Minors who are
# not eligible to work Group 2 : 18<Age<60 , ELigible to work Group 3 : >60, Too old to work as per govt. regulati
# ons

''''n=int(input('enter the number'))
if n>18:
    print(n,'elighble thhe work')
elif n<18:
    print(n,'not elighble the work')
else:
    print('elighble the work')'''
# -----------------------------------------------------
# REVERSE WORD
'''str1='SHIVAM SHRIVASTAVA'
rev_str1=""
for i in str1:
    # print(i)
    rev_str1=i+rev_str1
print(rev_str1)'''

# fo=open('C://Users//gj//Downloads//Microsoft Excel Comma Separated Values File .csv,'r'')
# data = fo.readlines()
# for i in data:
#     print(i)



# 2. Take two int values from user and print greatest among them
'''n1=int(input('enter the 1st number'))
n2=int(input('enter the 2nd number'))
if n1>n2:
    print(n1,'n1 is greatest number')
else:
    print((n2,'n2 is graetest number'))
print()'''

# . A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for use
'''sp=int(input('enter the sp'))
discount=int(input('enter the discount'))
quantity=int(input('enter the quantity'))
if quantity>1000:
    kk = (discount / sp) * 100
    discount = sp - kk
    print(discount)
else:
    print('no discount')'''

# 4. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

'''exp=int(input('enter the exp'))
salary=int(input('enter the salary'))
if exp>5:
    hh=(salary*5)/100
    total_salary=salary+hh
    print('get the bonous and total salary',total_salary)
else:
    print('not able the bonous')'''


# 5. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.


'''marks=int(input('enter the marks'))
if marks < 25:
    print('category f',marks)
elif marks > 25 and marks < 45:
    print('category E',marks)
elif marks > 45 and marks < 50:
    print('category D',marks)
elif marks > 50 and marks < 60:
    print('category C',marks)
elif marks > 60 and marks < 80:
    print('category B',marks)
else:
    marks >80
    print('category A',marks)'''

# 6. Take input of age of 3 people by user and determine oldest and youngest among them.

'''ag1=int(input('enter the age1'))
ag2=int(input('enter the age2'))
ag3=int(input('enter the ag3'))
if ag1>ag2 and ag1>ag3:
    print('ag1 is the oldest among of them',ag1)
elif ag2>ag1 and ag2 >ag3 :
    print('ag2 is the oldest among of them',ag2)
else:
    print("ag3 is the oldest among of them",ag3)
print()'''

# 8. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

'''nd =int(input('enter of the working days'))
na= int(input('enter the days of absent'))
per= (nd-na)/nd*100
print('your attendence is ',per)
if per <75 :
    print('you are not elighble for exam',per)
else:
    print('you are elighble for exam',per)'''


# 11. How to find the greatest amoung three numbers?

'''num1=int(input('enter the num1'))
num2=int(input('enter the num2'))
num3=int(input('enter the num3'))
if num1>num2 and num1>num3:
    print('num1 is the greatest among of them',num1)
elif num2>num1 and num2 >num3 :
    print('num2 is the greatest among of them',num2)
else:
    print("num3 is the greatest among of them",num3)
print()'''


# 12. How to find the smallest amoung three numbers?

'''num1=int(input('enter the num1'))
num2=int(input('enter the num2'))
num3=int(input('enter the num3'))
if num1<num2 and num1<num3:
    print('num1 is the smallest among of them',num1)
elif num2<num1 and num2 <num3 :
    print('num2 is the smallest among of them',num2)
else:
    print("num3 is the smallest among of them",num3)
print()'''


 # . A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for use

'''quantity= int(input('enter the quantity'))
if quantity*100 > 1000:
    kk=(quantity*100)
    kk2=10/100*kk
    total_price=kk-kk2
    print(total_price)
else:
    print('no change')'''


# Take values of length and breadth of a rectangle from user and check if it is square or not.

'''length=int(input('enter the length'))
breadth=int(input('enter the breadth'))
if length ==breadth:
    print('square')
else:
    print('rectangular')'''



# 7. Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

'''n1=int(input('enter the number'))
if n1>0:
    print(n1)
else:
    n2=n1*-1
    print(n2)'''

# 9. Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
# 10. If
# x = 2
# y = 5
# z = 0
# then find values of the following expressions:
# a. x == 2
# b. x != 5
# c. x != 5 && y >= 5
# d. z != 0 || x == 2
# e. !(y < 10)
'''x = 2
y = 5
z = 0

print(x == 2)
print(x != 5)
print(x != 5 and y >= 5)
print(z != 0 or x == 2)
print(not (y < 10))'''


# 1.print the sum and product from 1 to 20.
'''sum=0
pro=1
for i in range(1,21):
    # print(i)
    sum=sum+i
    pro=pro*i
print('sum=',sum)
print('pro=',pro)'''


# 2.print the numbers which is not divisible by 3 , from 1 to 20.

'''for i in range(1,21):
    # print(i)
    if i % 3 != 0:
        print('not divisible by 3 =',i)'''

# 3.print even numbers between 1 and 20.
'''for i in range (1,21):
    if i % 2 ==0:
        print('divisible by 2 =',i)'''

# 4.print average of numbers from 1 to 20 (should work for any numbers)
'''sum=0
count=0
for i in range (1,21):
     # print(i)
     count=count+1
     sum=sum+i
     print('average of sum =', i, sum / count)'''

# a.) write a program to check whether the number is palindrom or not ?

'''n=int(input('enter the number'))
rev=0
x=n
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
if (x==rev):
    print('palindrome')
else:
    print('not palindrome')'''

# write a program to take two integer value from user. and then tell which number
# is having the highest digit average.

'''num1 = int(input('enter the number'))
num2 = int(input('enter the number'))
sum1=0
count1=0
while (num1>0):
    sum1=sum1+num1%10
    num1=num1//10
    count1=count1+num1
average_1 = sum1/count1
# print(average_1)
sum2=0
count2=0
while (num2>0):
    sum2=sum2+num2%10
    num2=num2//10
    count2=count2+num2
    average_2 = sum2/count2
# print(average_2)
if average_1 > average_2:
    print('average_1',average_1)
elif average_2 >average_1:
    print('average_2',average_2)
else:
    print('equal average=',average_1,average_2)'''

# write a program to take a number and a digit from the user.and then
# findout that digit is coming how many times to that given number.



# letter captilization





# palindrome string

'''word = input('enter the number')
final_w = ""
for i in word:
    final_w = i + final_w

if (word == final_w):
    print("palindrome")
else:
    print("Not palindrome")'''



'''list1=[43,23,23,56,234,24]
max1=list1[0]
for i in list1:
    if i > max1:
        max1=i
print(max1)'''



# take a three input and find the greatest number
'''n1=int(input('enter the 1st number'))
n2=int(input('enter the 2nd number'))
n3=int(input('enter the 3rd number'))

if n1>n2 and n1>n3:
    print('n1 is greater',n1)
elif n2>n1 and n2 >n1:
    print('n2 is the greater',n2)
elif n3>n1 and n3 >n2:
    print('n3 is the greater',n3)
else:
    print('n1=n2=n3',n1,n2,n3)'''

# pint the sum and product from 1 to 20
'''sum=0
product=1
for i in range (1,21):
    # print(i)
    sum=sum+i
    product=product*i
print(sum)
print(product)'''

# print the number which is not divisible by 3 but divissible by 2 and 5
'''for i in range (1,21):
    # print(i)
    # if i%3!=0:
    #     print(i)
    if i %2==0 and i %5==0 and i% 3!=0:
  
        print('divisible by 2 and 5 ',i)'''


# prrint the even number between 0 to 20

'''for i in range(0,21):
    # print(i)
    if i % 2==0:
        print("all the even number",i)'''

# write a program to check whether a aperson is elighible for voting or not voting

'''voting_age =int(input('enter the number '))
if voting_age >18 or voting_age==18:
    print('elighble for voting',voting_age)
else:
    print('not elighble for the voting',voting_age)'''

# write a program to check whether a number is even or odd

'''n= int(input('enter the number'))
if n% 2==0:
    print('number is even number',n)
else:
    print('the numberis odd number',n)'''


# give 5 pythonexample that result in syntax error
'''a=5:
b=3
print(a+b)'''

'''$a4=8
b=5
print(a*b)'''

'''%=89
k=7
print(a-b)'''

'''54=45
12=50
print(45+50)'''

'''-A=7
B=8
print(A+B)'''

# add and prin 2 decimal number
'''a=2
b=35
print(a+b)'''

# add print 2 decimal number
'''a=20
b=30
kk='the value of a=%d'%a
kk2='the value of b=%d'%b
print(a+b)'''

# add two variable int ,float
'''a=324
b=356.00
print(a+b)'''

# add two variable int,boolean
'''a=6
b=True
print(a+b)'''

# add two variable one float one boolean
'''a=5.5
b=True
print(a+b)'''

# add two variable one float one complex

'''a=6.5
b=5+3j
print(a+b)'''

# add two variable one complex one int
'''a=56
b=67+4j
print(a+b)'''


# add two string in pyton
'''a='shivan'
b='shrivastava'
print(a+b)'''

# add two float number

'''a=5.5
b=6.5
print(a+b)'''

# wap 2 octal nummber
'''a=0o101
b=0o101
print(a+b)'''

# wap 2 hexa number

'''a=0x11
b=0x12
print(a+b)'''
 # wap to hexa decimalnumbeer upper case
'''a=0X101
b=0X101
print(a+b)'''

# wap to reverse number

'''n=int(input('enter the number'))
rev=0
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
print('reverse number =', rev)'''

# wap to check a number palindrome number or not

'''n=int(input('enter the number'))
rev=0
f=n
while n>0:
    rev=(rev*10)+n%10
    n=n//10
if rev==f:
    print('this number is palindrome number ')

else:
    print('this number is not a palindrome number')'''

# A shop will give discount of 10% if the cost of purchage quanity ismorethan 1000
# ask user for quaninty
# suppose ,one unit will cost 100
# judge and print total cost ofuser


'''quaninty=int(input('enter the quaninty'))
if quaninty*100>1000:
    kk=quaninty*100
    kk2=10/100*kk
    total_price=kk-kk2'''