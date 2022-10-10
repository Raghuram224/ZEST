def numbers(n):
    a=[]
    total =0
    for i in range(n):    
        value =input()
        a.append(value)
        a.append(";")    
    for i in a:
         print(i,end="")    
    for i in a:
        if i==";":
            a.remove(i)
    result = a
    result= list(map(int, result))
    for i in result:        
        total=total+i
    print("output is:",+total)

numbers(3) #this is how many inputs you need to enter










