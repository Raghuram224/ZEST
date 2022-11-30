#another solution
import string
def rangoli(n):
    st=string.ascii_lowercase   
    l=[]
    for i in range(n):
        s='-'.join(st[i:n])    # join will add - in a-b-c
        l.append((s[::-1]+s[1:]).center(4*n-3,'-')) #this - add in ----c---
    print(l)
    j=1
    for i in range(n):
        print(l[n-j])
        j+=1
    for i in range(n-1):
        print(l[i+1])     

rangoli(3)
#old code
def rangoli_alpha(n):
    al = list(map(chr,range(97,123)))    
    x=al[n-1::-1]+al[1:n]   #reverse la varum c b a + b c n-1::-1 reverse la value c b a
    
    width=len('-'.join(x)) #width c-b-a-b-c total 9
    for i in range(1,n):
        print('-'.join(al[n-1:n-i:-1]+al[n-i:n]).center(width,'-')) #the first part remains empt and 
        #second part n-0:n c and n-1:n == b c
    for j in range(n,0,-1): # reverse 3 2 1start stop increment/ step
        print('-'.join(al[n-1:n-j:-1]+al[n-j:n]).center(width,'-')) #j will be 3 and 2:0:-1 +0:3 c b +a b c
    
n=3
rangoli_alpha(n)
