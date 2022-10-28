def modulo(n):
    for i in range(1,n):
        for  j in range(1,n):
            k=i*j%n
            print(k,end=' ')
        print()

modulo(n=int(input('Enter n:')))
