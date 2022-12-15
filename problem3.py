def is_prost(num):
    num = int(num)
    for i in range(num):
        if (num % i == 0):
            return False
    return True
num = 600851475143
i = 2
list = []
while (num != 1):
    if (num % i == 0):
        list.append(i)
        num /= i
    i += 1
l = len(list) - 1
print(list[l])