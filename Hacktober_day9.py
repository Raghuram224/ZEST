def numerical_value(n):    #97 is asci value of a 97-1=96 to reverse that
    total=0    
    a=[]    
    for i in n.lower():
        a.append(ord(i)-96)   
    for i in a:
        total=total+i
    print(total)
numerical_value("dave") #input in string