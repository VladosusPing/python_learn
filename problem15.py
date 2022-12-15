def compute(x):
    all_kletki = (x + 1) * (x + 1)
    sum_var = []
    for i in range(all_kletki):
        if (i % (x + 1) == 0) or (i < (x + 1)):
            sum_var.append(1)
        else:
            sum_var.append(0)
    for i in range(x + 1, all_kletki):
        if sum_var[i] == 0:
                sum_var[i] = sum_var[i - 1] + sum_var[i - x - 1]
    print(sum_var[len(sum_var) - 1])


compute(20)