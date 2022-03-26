def calculate(n1,n2,operator):
    switcher={
        '+':lambda n1,n2:n1+n2,
        '-':lambda n1,n2:n1-n2,
        '*':lambda n1,n2:n1*n2,
        '/':lambda n1,n2:n1/n2
        }

    return switcher.get(operator)(n1,n2)
print(calculate(10,20,'+'))
print(calculate(10,20,'-'))
print(calculate(10,20,'*'))
print(calculate(10,20,'/'))
