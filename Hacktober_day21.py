
def func_main(str1,char,index,):
    if str1[index]==char:
        print("True")
        return False
    else:
        index+=1                 
    if index<(len(str1)): 
            return func_main(str1,char,index) 
    else:
        print("False")
        return False        
func_main(str1=input('String:'),char=input('Char:'),  index=0)