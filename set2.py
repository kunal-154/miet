months={"January","Febuary","March","April","May","June"}
print(months)
#months.add("June","July")  #error: set.add() takes exactly one argument (2 given)
#print(months)
#months.discard("july")   july ni h lekin tb bhi error ni dega
months.remove("July")    #KeyError: 'July' (july ni h uppr set mai isliye error dega)
print(months)


months.add("July") # will add july
print(months)

months.update(["August","September","October","November","December"]) #set.update()can add many elemnets
print(months)


for i in months:
    if(i=="Febuary" or i=="March"):
        months.remove(i)
print(months)

    
