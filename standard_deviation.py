mean = 0.0
std_var = 0.0

ary1_len = int(input())
ary1 = [float(s) for s in input().split()]

for x in ary1:
    mean += x
mean = mean/ary1_len

for x in ary1:
    std_var += ((x - mean) ** 2)

print(round(((std_var / ary1_len) ** 0.5), 1))