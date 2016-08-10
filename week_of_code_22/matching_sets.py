

n = int(raw_input())
x = [int(i) for i in raw_input().split(' ')]
y = [int(i) for i in raw_input().split(' ')]

x.sort()
y.sort()

z = [i - j for i, j in zip(x, y)]

if sum(z) != 0:
    print -1

else:
    print sum([abs(i) for i in z]) / 2
