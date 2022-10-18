
def main_func(list1,rows, columns):
        result=[]               
        start = 0
        end = columns
        for i in range(rows): 
            result.append(list1[start:end])
            start +=columns
            end += columns        
        for i in result:
            for j in range(len(i)):
                print(i[j],' ',end='')
            print()


n=int(input())
arr=[]
for i in range(n):
    for j in range(n):
        if(i == 0 or i == n - 1 or j == 0 or j == n - 1
           or i == j or j == (n - 1 - i)):
            a=arr.append('#')
        else:
            a=arr.append(' ')
main_func(arr, n, n)