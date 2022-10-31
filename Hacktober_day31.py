
def minesweeper(n,m):
    import random
    ran=[0,'M']
    array = [[0 for column in range(m)] for row in range(n)]
    for i in range(n):
        for j in range(m):
            array[i][j]=random.choice(ran)

    for a in array:
        for val in a:
            print(val,end=' ')
        print()

    for i in range(n):
        for j in range(m):
            if(array[i][j]==0):
            
                if i-1 >=0 and j -1 >=0 and 'M' == array[i-1][j-1]:
                    array[i][j]+=1
            
                if i-1 >=0 and j+1 <=m-1 and 'M' == array[i-1][j+1] :
                    array[i][j]+=1

                if i-1 >=0 and 'M' ==  array[i-1][j] :
                    array[i][j]+=1

                if i+1 <=n-1 and 'M' == array[i+1][j]:
                    array[i][j]+=1  
                
                if i+1 <=n-1 and j-1 >=0 and 'M' == array[i+1][j-1] :
                    array[i][j]+=1
                    
                if i+1 <=n-1 and j+1 <=m-1 and 'M'==array[i+1][j+1] :
                    array[i][j]+=1
                    
                if j-1>=0 and 'M'==array[i][j-1] :
                    array[i][j]+=1
                    
                if j+1 <= m-1 and 'M' == array[i][j+1]:
                    array[i][j]+=1

    print('\n Result \n')
    for ar in array:
        for val in ar:
            print(val,end=' ')
        print()

if __name__=='__main__':
    minesweeper(n= int(input("Enter n:")), m=int(input("Enter m:")))