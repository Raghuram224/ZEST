def block_of_letter(n):
    res = ""
    for ind in range(97, 97 + n):
        res = res + chr(ind)
    w = res
    line = ''
    for i, j in enumerate(w):
        line = w[i:]+w[:i]
        print(line)

block_of_letter(26)
