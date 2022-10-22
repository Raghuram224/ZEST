
def func_main(s,t,n,m):
    if(s[n]!=t[m]):
        return n
    if s[n]==t[m]:
        n+=1
        m+=1
    if (n>len(s)-1 or m>len(s)-1):
        return m
    if m<=len(t):    
        return func_main(s,t,n,m)           
print(func_main(s=input('String1:'),t=input('String2:'),n=0,m=0))