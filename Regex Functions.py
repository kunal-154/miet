import re
txt="The rain in spain"
x=re.search("\\s",txt)  #(3,4) space sbse pehle 3 pr h or 4 pr khtm h
print(x)
print("The white space character is located in Position: ",x.start()) # starting index of space
print("The white space character is located in Position: ",x.end())   # ending index of space
print("The white space character is located in Position: ",x.group()) # jo hum search kr rhe h vhi print krega


x=re.findall('ain',txt) # it returrns list of ain or jitni br aa rhi h txt mai utni br list mai dikhayga
print(x)

x=re.split("\\s",txt)  # returns the list by spliting the element jo humne dala h vha se(space) 
print(x)

x=re.split('i',txt)  # ab split hoga jha jha i h vha se
print(x)

x=re.sub("\\s","9",txt) # space ko 9 se replace kr dia
print(x

