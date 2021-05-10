def gcd(u, v):
    while u > 0:
        if u < v:
            u, v = v, u
        u = u % v  # or subtraction
    return v


u_test = 84
v_test = 231
print(gcd(u_test, v_test))
