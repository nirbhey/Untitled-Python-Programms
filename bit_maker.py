n = 3
flag = []
for i in range(n):
    flag.append(0)

for i in range((2**n)):
    c = 2
    if i > 1:
        for z in range(1, n):
            #print(i, c)
            if i % c == 0:
                if flag[-z - 1] == 0:
                    flag[-z - 1] = 1
                else:
                    flag[-z - 1] = 0
            c = c * 2
            if c > i:
                break

    print(flag)

    if flag[-1] == 0:
        flag[-1] = 1
    else:
        flag[-1] = 0
