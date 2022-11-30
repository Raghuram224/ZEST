   #another code

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
    arr=array
    for i in range(n):
        for j in range(m):
            if arr[i][j]!="M":
                temp=0
                if i+1<n:
                    if arr[i+1][j]=='M':#bottom
                        temp+=1
                if j+1<m:               #right
                    if arr[i][j+1]=="M":
                        temp+=1
                if (i-1)>-1:
                    if arr[i-1][j]=='M':#top
                        temp+=1
                if (j-1)>-1:
                    if arr[i][j-1]=='M':#left
                        temp+=1
                if i+1<n and j+1<m: #right bottom
                    if arr[i+1][j+1]=='M':
                        temp+=1
                if (i-1)>-1 and (j-1)>-1:
                    if arr[i-1][j-1]=='M': #upper left
                        temp+=1
                if i+1<n and (j-1)>-1:
                    if arr[i+1][j-1]=='M':#left bottom
                        temp+=1
                if (i-1)>-1 and j+1<m: #upper right
                    if arr[i-1][j+1]=='M':
                        temp+=1
                arr[i][j]=str(temp)
    print('\n Result \n')
    for ar in array:
            for val in ar:
                print(val,end=' ')
            print()



minesweeper(5, 4)

#old code
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
            
                if i-1 >=0 and j -1 >=0 and 'M' == array[i-1][j-1]:#upper left
                    array[i][j]+=1
            
                if i-1 >=0 and j+1 <=m-1 and 'M' == array[i-1][j+1] : #upper right
                    array[i][j]+=1

                if i-1 >=0 and 'M' ==  array[i-1][j] :#top
                    array[i][j]+=1

                if i+1 <=n-1 and 'M' == array[i+1][j]:#bottom
                    array[i][j]+=1  
                
                if i+1 <=n-1 and j-1 >=0 and 'M' == array[i+1][j-1] :#bottom left
                    array[i][j]+=1
                    
                if i+1 <=n-1 and j+1 <=m-1 and 'M'==array[i+1][j+1] : #bottom right
                    array[i][j]+=1
                    
                if j-1>=0 and 'M'==array[i][j-1] : #left
                    array[i][j]+=1
                    
                if j+1 <= m-1 and 'M' == array[i][j+1]: #right
                    array[i][j]+=1

    print('\n Result \n')
    for ar in array:
        for val in ar:
            print(val,end=' ')
        print()

if __name__=='__main__':
    minesweeper(n= int(input("Enter n:")), m=int(input("Enter m:")))
    
    
