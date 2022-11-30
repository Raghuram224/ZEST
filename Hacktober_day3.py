def reverse_num(N):
    output=0
    while(N>0):
        reminder = N % 10
        output = int((output*10)+reminder)
        N //=10       
    print(output)
    
reverse_num(5678) #here you can test input
