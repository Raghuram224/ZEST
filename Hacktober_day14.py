#another solution
def block_of_letter(n):
    res = ""
    for ind in range(97, 97 + n):
        res = res + chr(ind)
    w = res
   
    for i in range(n):        
        print(w[i:]+w[:i])
    


def block_of_letter(n):
    res = ""
    for ind in range(97, 97 + n):
        res = res + chr(ind)
    w = res
    line = ''
    
    for i, j in enumerate(w): #i=0 and j=a
        line = w[i:]+w[:i]      #bcde +a
        print(line)

block_of_letter(5)
