num = 1
while(True):
    num += 1
    if num * num > 1000:
        num -= 1
        break
prov = False
for i in range(1, num):
    for j in range(1, num):
        for k in range(1, num):
            if (i*i + k*k + j*j == 1000):
                print('a = ', i, 'b= ', j, 'c = ', k)
                prov = True
                break
        if prov == True:
            break
    if prov == True:
        break

