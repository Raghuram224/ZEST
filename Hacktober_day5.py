a,b,c = map(int,input().split()) #here you can enter inputs
Triangle=180
if (a and b and c > 0):
    if(a+b+c==Triangle):
        print("true")
    else:
        print("false")
else:
    print("false")
    
