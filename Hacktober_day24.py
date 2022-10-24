
def digital_root(n,count,i):
    if len(str(n))==len('1'):
        return n
    n=str(n)    
    count+=int(n[i])    
    i+=1
    if len(str(n))==i:
        if len(str(n))==len('1'):            
            return count
        n=count
        i=0
        count=0        
        digital_root(n, count, i)   
    return digital_root(n, count, i)
print(digital_root(n=input('Enter int:'),count=0,i=0))
