def euler_5():
    num = 20
    while(True):
        if (num % 9 == 0) and (num % 19 == 0) and (num % 17 == 0)and (num % 13 == 0) and (num % 11 == 0) and (num % 16 == 0) and (num % 14 == 0):
            print(num)
            break
        num += 10
euler_5()