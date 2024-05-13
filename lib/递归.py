def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)

print(sum(6))

def cheng(u):
    if u == 0:
        return 1
    else:
        return u*cheng(u-1)

print(cheng(5))

def chu(a):
    if a == 0:
        return 1
    else:
        return a/chu(a-1)

print(chu(6))