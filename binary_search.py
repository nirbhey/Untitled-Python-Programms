def binary_search(listx, ele):
    try:
        mid = int(len(listx) / 2)
        if listx[mid] == ele:
            print("Present!")
            return int(mid)
        if listx[mid] > ele:
            binary_search(listx[:mid], ele)
        if listx[mid] < ele:
            binary_search(listx[mid + 1:], ele)
    except Exception as e:
        print("Not present!")
        return None

listx = [0, 1, 2, 3, 4, 5, 6, 7]
listx.sort()
print(listx)
x_at = int(input('Enter the element you want to search in a sorted list!') )
binary_search(listx, x_at)

""" Without resurrection, better for python! :/
def binary_search(listx, val):
    lo, hi = 0, len(listx) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if listx[mid] < val:
            lo = mid + 1
        elif val < listx[mid]:
            hi = mid - 1
        else:
            return mid
    return None

listx = [1, 2, 3, 31231, 5, 6, 62,26,2,2,2,3232,4242]
listx.sort()
print(listx)
val = int(input('Enter the number you want to search!'))
mid = binary_search(listx, val)
print(mid)
"""