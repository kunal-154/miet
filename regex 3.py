"Pattern Matching"

import re
txt = "Hello planet"
x=re.findall("planet$",txt)  # $ means planet se end hua h  or  ^ means starting word h
if x:
    print("Yes, The string ends with 'planet'")
else:
    print('no match')


x=re.findall("He.*o",txt)  # * lgane se multiple dots ki need ni h ek se hi kaam ho jayga
print(x)
