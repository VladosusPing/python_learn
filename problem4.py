def pol6(num):
    if (num %10 == (int(num / 100000) % 10)):
        if ((int(num / 10) % 10) == (int(num / 10000) % 10)): 
            if ((int(num / 100) % 10) == (int(num / 1000) % 10)): 
                return True
    return False

bp = False

for i in range(999, 100, -1):
    for j in range(999, i, -1):
        if (pol6(i*j) == True):
            print(i*j)
            bp = True
            break
    if (bp == True):
        break