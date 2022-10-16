
def ounces_to_pounds(ounce):
    pounds=ounce//16
    ounces=ounce%16
    print("{} Pounds,{} ounces".format(pounds,ounces))

ounce=int(input())
ounces_to_pounds(ounce)
