
def sequence(a):
    total = 0
    ans = a.split(";")
    for i  in ans:
        total+=int(i)
    print(total)
sequence("5;7;1") #enter inputs in string

