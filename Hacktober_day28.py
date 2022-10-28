# input from same line with separate space like 2 3 4 5 -6
def consecutive_num(l,i,count):    
    if i== len(l)-1:
        if count>0:
            return True
        else:
            return False
    if i<len(l)-1:
        a=l[i]
        b=l[i+1]  
        if a+b==0:        
            count+=1        
        i+=1
    return consecutive_num(l,i,count)
print(consecutive_num(l=[int(x) for x in input('Enter:').split()],i=0,count=0))