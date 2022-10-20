
def func_main(n,count,index,):
    if n[index] ==n[index+1]:
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
func_main(n=str(input()), count=1, index=0)
