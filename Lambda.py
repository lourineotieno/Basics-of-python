#lambda functions takes any number of arguments, but can only have one expression.
x=lambda a: a+10
print(x(5))
x=lambda a,b: a*b
print(x(6,19))
def  my_function(n):
    return lambda a: a*n
mydoubler=my_function(2)
print(mydoubler(11))