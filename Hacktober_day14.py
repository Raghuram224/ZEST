def alphabet(N):
    res = []
    nes=[]
    for idx in range(97, 97 + N):
       r = res.append(chr(idx))
    #print(res)
    count=0
    for i in range(3):
        for j in range(26):
            a=res[j]
            m=a[0:j]+a[j:]
            print(m,end="")
        print()
        count+=1        
alphabet(26)