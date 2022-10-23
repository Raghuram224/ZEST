
def recursive(s,index):
    a=s[index]
    if a=='0'or a=='1':                
        index+=1    
    elif a!='0'or a!='1':        
        return False   
    if index==len(s):
            return True    
    return recursive(s, index)    

print(recursive(s=str(input('String:')), index=0))