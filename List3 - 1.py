n = int(input('適当に\n>'))
s = 5
if n > 0:
    print('{}は正の値'.format(n))
elif n == 0:
    print('{}は0desu'.format(n))
elif n == -10:
    pass
else:
    print('{}はウンチです'.format(n))

print('s < n =',s < n)
