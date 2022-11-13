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






def check_board(n):
    import numpy as np
    a = np.array([1])
    x = np.tile(a,(n,n)) #try to understand numpy
    x[1::2, ::2] = 2
    x[::2, 1::2] = 2 # understand the list slicing
    for i in x:
        for i in i:
            print(i,"",end="")
        print()

check_board(n = int(input()))
