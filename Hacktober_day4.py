def find_sec_large(a,b,c):
    if(a>b& a>c):
        if(b>c):
            print (b) 
        else:
            print(c) 
    elif (b>c & b>a):
        if(a>c):
            print(a)
        else:
            print(c)
    else:
        if(a>b):
            print(a)   
        else:
            print(b)
            
a,b,c = map(int,input().split())
find_sec_large(a,b,c)
