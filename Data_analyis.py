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
fo = open('C:\\Users\\gj\\Downloads\\data (1).txt', 'r')
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
print(dict1)