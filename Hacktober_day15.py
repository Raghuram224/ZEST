# like pyramid pattern it will easy ensure reverse and add in doube (())
# import string
# def rangoli(n):
#     l=[]
#     st=string.ascii_lowercase
#     print(st)
#     for i in range(n):
#         s='-'.join(st[i:n])
#         l.append((s[::-1]+s[1:]).center(4*n-3,'-'))    
#     j=1
#     for i in range(n):
#         print(l[n-j])
#         j+=1
#     for i in range(n-1):
#         print(l[i+1]) 

# rangoli(3)
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
