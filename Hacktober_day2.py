def sum_of_first_last(inp):
    a =[]
    while inp>0:
        reminder = inp%10
        a.append(reminder)
        inp = inp//10
    a=list(reversed(a))
    print(a[0]+a[-1])
sum_of_first_last(4001)