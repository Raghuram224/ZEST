

def add_one_to_everything(a=[]):
    c=[]
    count=len(a)
    def main(count,a):
        if count-1>-1:
            d=a[count-1]+1
            c.append(d)
            count-=1
            main(count,a)
        else:
            m=c.reverse()
            print(c)
    main(count,a)

add_one_to_everything([2,6,3,8])