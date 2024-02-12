#if statement
a=20
x =20
if x>a:
    print("x is greater than a")
elif x<a:
    print('x is less than a')
else:
    print("x is equal to a")

    #while loop
    i=5
    while i<10:
        print(i)
        if i==8:
            break
        i+=1
    else:
        print("i is no longer less than 10")

        #for loop
    fruits=["apple","orange",'banana',"berry"]
    for i in fruits:
            if i=="banana":
                break
            print(i)

            for x in range(10,20,2):
                 print(x)
            else:
                 print("finally finished!")
            