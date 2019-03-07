#include <stdio.h>
#include <stdint.h>

uint64_t mul_mod(uint64_t a, uint64_t b, uint64_t m)
{
   uint64_t d = 0, mp2 = m >> 1;
   int i;
   if (a >= m) a %= m;
   if (b >= m) b %= m;
   for (i = 0; i < 64; ++i)
   {
       d = (d > mp2) ? (d << 1) - m : d << 1;
       if (a & 0x8000000000000000ULL)
           d += b;
       if (d >= m) d -= m;
       a <<= 1;
   }
   return d;
}


uint64_t pow_mod(uint64_t a, uint64_t b, uint64_t m)
{
    uint64_t r = m==1?0:1;
    while (b > 0) {
        if(b & 1)
            r = mul_mod(r, a, m);
        b = b >> 1;
        a = mul_mod(a, a, m);
    }
    return r;
}


int main()
{
    int a = 1777;
    for (int i = 0; i < 1855; ++i) {
        a = pow_mod(1777, a, 100000000);
    }
    printf("%d", a);
    return 0;
}
