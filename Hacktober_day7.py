import calendar
def checkyear(year):
    return(calendar.isleap(year))
year = int(input())
if checkyear(year):
    print("true")
else:
    print("false")
