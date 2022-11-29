#another solution
def word_extend(word):
    l=len(word)-1
    if l==0:
        return word
    else:
        m=(l+2)//2 #5 input will be 3
        print(m)
        n=m
        temp1=''
        temp2=''

        for i in range(m):
            temp1+=word[i]*n #3*a
            temp2+=word[l]*n  #3*e
            l-=1
            n-=1
        # print(temp1[:1])
        # print(temp2[::-1])
        print(temp1[:-1]+temp2[::-1])


import math
def program_word():    
    txt=str(input())
    if(len(txt)%2!=0): #it check even or odd input
        a=[]
        for i in txt:
            a.append(i)    
        index=math.floor(len(txt)/2)  
        slice_left = index+1
        slice_right = 2
        i =0
        while(i<len(txt)):
            if(i==index):
                n=0
                while(n<1):
                    print(a[i],end="")
                    n+=1
            elif(i<index):
                j=0
                while(j<slice_left):
                    print(a[i],end="")
                    j+=1
                slice_left-=1
            
            elif(i>index):
                m=0
                while(m<slice_right):
                    print(a[i],end="")
                    m+=1
                slice_right+=1
            i+=1
            
program_word()

        
