from strah import is_prime


c = 49
n = 8
tot = 13
step = 8
while n / tot > 1 / 10:
    c += step
    n += is_prime(c)
    
    c += step
    n += is_prime(c)
    
    c += step
    n += is_prime(c)
    
    c += step
    n += is_prime(c)
    
    step += 2
    tot += 4
    #print(n / tot)

print(step - 1, c, n, n / tot)
