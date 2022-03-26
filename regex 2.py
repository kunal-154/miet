""" Forming a Regular expression"""


import re
txt="The rain in spain"
x=re.findall("[a-m]",txt)  # a-m ke beech mai jitne character h small vale vo return krega
print(x)

x=re.findall("[a-zA-Z]",txt)  # inke beech mai jo jo charcater h unko search krega
print(x)


text="hello planet"
x=re.findall("he..o",text)  # jitni . h utne hi match krega
print(x)

a='helllooo'
y=re.findall('he..o',a) #  empty set qki . km h or lll zada
print(y)
