
def isPalindrome(s):
    b=s[::-1]       
    if s==b:
        print("true")
    else:
        print("false")

isPalindrome(str(input()))