listx = [0, 2, 3, 4, 5, 6]
f = 1
while f != 'q':
    print(listx)
    print("Enter the element to access!")
    x = int(input())
    idx = listx.index(x)
    if idx == (len(listx) - 1):
        listx[:] = [listx[idx]] + listx[:idx]
    else:
        listx[:] = [listx[idx]] + listx[:idx] + listx[idx+1:]
    print(listx)
    f = input("press 'q' to quit (or) any other key to continue")