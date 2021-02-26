#Add Digits

num = 38

def y(num):

    num = list(str(num))
    q = 0
    
    while int(len(num)) != 1:
        for i in range(int(len(num))):
            q = int(num[i]) + q

        num.clear()
        num = list(str(q))
        q = 0
    
    return num[0]

print(y(num)) 
