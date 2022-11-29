
def print_letter(word):    
    for i in range(len(word)):
        print(word[:i+1]+" ",end="")

print_letter(str(input()))
