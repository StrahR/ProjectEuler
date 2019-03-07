from strah import sieve

target = 1000000
primes = sieve(target)

#print(primes)

ml = 0
mp = 0

for p in primes:
    print(p)
    st = 0
    l = 1
    s = primes[0]
    while s < p:
        s += primes[st + l]
        l += 1
    while primes[st + l] < p:
        while l <= ml and st + l + 1 < len(primes):
            l += 1
            s += primes[st + l]
        #print(s, l)
        while s < p:
            s += primes[st + l]
            l += 1
        if s == p:
            if l > ml:
                ml = l
                mp = p
                #print(p, primes[st], st, l)
            break
        
        while s > p:
            s -= primes[st]
            st += 1
            l -= 1
        if s == p:
            if l > ml:
                ml = l
                mp = p
                #print(p, primes[st], st, l)
            break
print(mp, ml)
