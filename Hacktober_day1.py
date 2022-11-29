def find_ans(num,x):
    count=0
    while num!=0:
        reminder= num%10
        if reminder==x:
            count+=1
        num = num//10
        
    print(count)

find_ans(664,4)
