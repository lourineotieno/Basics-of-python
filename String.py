a="hello world!"
print(len(a))
#checking string
txt="school of computing and informatics"
print("on" in txt)

#if statements
txt="school of computing and informatics"
if "school" in txt:
    print("yes, 'school' is present.")
    
    #modifyinng string
    a="hello world"
    print(a.upper())
    print(a.lower())

    #Replacing string
    a='hello world!'
    print(a.replace("h", 'm'))

#split string
    a='hello world!'
    print(a.split(","))

    #string combination
    a="school"
    b="of"
    c="computing"
    d=a +  " "+b +" "+ c
    print(d)

    #string format
    age=21
    txt="My name is Lourine, and i am {} years old"
    print(txt.format(age))
    quantitty=2
    itemno=2
    price=56.20
    myorder="I want to pay {2} shillings for {0} pieces of item {1}"
print(myorder.format(quantitty,itemno,price))


thislist=["apple",'orange',"melon"]
thislist[1]="cherry"
thislist.append("banana")
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1
    