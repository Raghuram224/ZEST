
def count(n):
    from random import randint    
    if n<=100:    
        count=0
        matrix = [[]*n for i in range(n)]
        for o in range(n):
            for k in range(n):
                ran=randint(1, 5)
                matrix[o].append(ran)
        for i in matrix:            
            print(i)
        count =0
        for i in matrix:                
                for j in range(len(i)) :                    
                    if (i[j])==5:
                        count+=1
        print("count's of 5:",count)
count(n=int(input()))

