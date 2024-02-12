def greet(name):
 print("hello", name)
#call function
#greet('lourine')

#parameters and arguments
    
def my_function(fname,lname):
 print(fname +" " +lname)

#my_function('Lourine','refsnes')

        #Arbitrary arguments
def my_function(*active_children):
 print("The younger child  present is" +active_children[1])
#my_function('lourinwe',"emilly")
            #default parameter value
def my_function(country="Kennya"):
 print("i am from " +country)
my_function("uganda")
my_function("Tanzania")