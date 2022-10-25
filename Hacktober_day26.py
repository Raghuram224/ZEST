
def bitFlip(s,i,l):
    if s[i]=='0':
        l=l+'1'
    elif s[i]=='1':
        l=l+'0'
    else:
        return False
    i+=1
    if i==len(s):
        return l
    return bitFlip(s,i,l)

print(bitFlip('101010',i=0,l=''))