
def OneAway(s,t,i,count):
    if s==t:
        return False
    if len(s)==len(t):        
        if s[i]!=t[i]:
            count+=1        
        i+=1
        if i==len(s):
            if count>1:
                return False
            if count==1:
                return True
        return OneAway(s,t,i,count)
    else:
        return False

print(OneAway('water', 'wafer',i=0,count=0))