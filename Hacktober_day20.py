
def func_main(n,count,index,):
    a=n[index]        
    b=n[index+1]
    if a==b:
        count+=1
    else:
        index+=1
    if count==2:
        print("True")
        return False             
    if index<(len(n)-1): 
            return func_main(n,count,index) 
    else:
        print("False")
        return False        
func_main('bcddef', count=1, index=0)