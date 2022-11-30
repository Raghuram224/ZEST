def check_board(n): # this is an another patter for  check board
    l=[]    
    for i in range(n):
        test=[]
        for j  in range(n):
            r=i+j
            if r%2==0:
                test.append(1)
            else:
                test.append(2)
        l.append(test)
    for i in l:
        for j in i:
            print(j,end=' ')
        print()       

check_board(5)

#old code

def check_board(n):
    import numpy as np
    a = np.array([1]) #normal list
    print(a)
    x = np.tile(a,(n,n)) #it will creatte nxn array a wil be value of 1
    x[1::2, ::2] = 2  #1 la irukuradhu 2 row 1::2 and ::2 every 2 element will be 2
    x[::2, 1::2] = 2 # ::2 1 la irukuradhu every 2 row ku munnadi 1 st row 1:: 2 element will be 2
    for i in x:
        for i in i:
            print(i,"",end="")
        print()

check_board(n = int(input()))
 


