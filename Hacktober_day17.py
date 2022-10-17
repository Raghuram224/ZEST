
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