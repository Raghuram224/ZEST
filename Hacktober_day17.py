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
    a = np.array([1]) #normal list
    print(a)
    x = np.tile(a,(n,n)) #it will creatte nxn array a wil be value of 1
    x[1::2, ::2] = 2  #it  wil add even rows with num 2 one after another
    x[::2, 1::2] = 2 # it will add odd rowss with num 3 one after another
    for i in x:
        for i in i:
            print(i,"",end="")
        print()

check_board(n = int(input()))



 


