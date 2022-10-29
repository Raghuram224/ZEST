
# input from same line with separate space like 1 1 2 3
def sameElements(l1,l2,i):    
    if len(l1) == len(l2):
        l1.sort()
        l2.sort()
        if i==len(l1):
            return True
        if l1[i]==l2[i]:
            i+=1
        else:
            return False   
    else:
        return False 
    return sameElements(l1, l2, i)

print(sameElements(l1=[int(x) for x in input('Enter list 1:').split()],l2=[int(x) for x in input('Enter list 2:').split()],i=0))
