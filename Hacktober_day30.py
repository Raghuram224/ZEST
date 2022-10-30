
import random as rand
import math
n=int(input('Enter n:'))
arr=[]
check=[]

if (n%2==0): #even input
    for j in range(n//2): #it will divide the output  to one side
        for i in range(n):      
            ran=(chr(rand.randrange(33,94)))                 
            arr.append(ran)

    check = [*set(arr)]    
    if len(arr)!=len(check): #it will remove if any double and add new 
        for i in range(len(arr)-len(check)):      
                ran=(chr(rand.randrange(33,94)))                 
                check.append(ran)

    lst1 = check+check    
    rand.shuffle(lst1)
    m = []
    while lst1 != []: #create nxn list
        m.append(lst1[:n])
        lst1 = lst1[n:]  

    for i in m: #output
        for j in i:
            print(j,end=' ')
        print()

elif(n%2==1): #odd input
    i=0
    string=""    
    while(i<math.ceil(n**2/2)):        
        ran = chr(rand.randrange(33,94))        
        if ran not in string:
            arr.append(ran)
        else:
            i-=1            
        i+=1
    
    check = [*set(arr)]       
    if len(arr)!=len(check): #it will remove if any double and add new 
        for i in range(len(arr)-len(check)):      
                ran=(chr(rand.randrange(33,94)))                 
                check.append(ran)    

    test=check.copy()    
    del test[-1]    #make odd list of one side
    if n%2 == 1:
        check=check[:]
   
    check=check+test      
    rand.shuffle(check)
    lst1=check
    m = []
    while lst1 != []: #create nxn list
        m.append(lst1[:n])
        lst1 = lst1[n:]     
    
    for i in m: #output
        for j in i:
            print(j,end=' ')
        print()