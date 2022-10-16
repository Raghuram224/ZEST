
def rangoli_alpha(n):
    al = list(map(chr,range(97,123)))    
    x=al[n-1::-1]+al[1:n]   
    width=len('-'.join(x))
    for i in range(1,n):
        print('-'.join(al[n-1:n-i:-1]+al[n-i:n]).center(width,'-'))
    for j in range(n,0,-1):
        print('-'.join(al[n-1:n-j:-1]+al[n-j:n]).center(width,'-'))
    
n=3
rangoli_alpha(n)
