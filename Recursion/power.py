def p(m,n):
    if n == 0:
        return 1
    else:
        return m * p(m, n-1)
print(p(3,2))

