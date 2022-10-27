input1,v=int(input("enter:")),[]
for i in range(1,input1+1):
    v.append(i)

n=v*input1
print(n)
print(n[8])
for r in range(1,input1):
    for c in range(1,input1):
        x=r*c
        # print(x)
        if x<input1:
            e=''
        else:
            if x<input1*10:
                e=''
        print(e,n[x-1],end='')
    # print(x)
    print()