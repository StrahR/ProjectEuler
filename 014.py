m_steps = 0
m_num = 0
steps = 0
num = 0


def collatz(n):
    global steps
    global m_steps
    global m_num
    steps += 1
    if n == 1:
        if steps > m_steps:
            m_steps = steps
            m_num = num
        return
    if n % 2 == 0:
        return collatz(n/2)
    else:
        return collatz(3*n + 1)


for i in range(1, 1000000):
    steps = 0
    num = i
    collatz(i)
print(m_num)  # 837799
