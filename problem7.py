def is_digit(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


i = 2
num = 3
while i < 10001:
    if is_digit(num):
        i += 1
    num += 1
print(num)
