t = []
for i in range(10 ** 6):
    t.append(i)

v = [x[1] - x[0] for x in zip(t[1:], t[:-1])]

v.sort()

print(v[-1])