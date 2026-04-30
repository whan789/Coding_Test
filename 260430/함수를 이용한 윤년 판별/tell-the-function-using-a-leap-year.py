y = int(input())

# Please write your code here.
def sol(year):
    if (year % 100 == 0) and (year % 400 !=0):
        return False
    if year % 4 ==0:
        return True

    return False

if sol(y):
    print('true')
else:
    print('false')