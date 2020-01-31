a = 2
b = 2
c = 1

if (a == b) == c:
    print('onazi')

tuki = int(input('月は？'))

if tuki in {1, 2, 3}:
    print('１２３月')

tuki = b if tuki < c else c
print(tuki)
