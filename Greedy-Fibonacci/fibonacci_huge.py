# Uses python3
import sys

def pisanoPeriod(m):
    previous = 0
    current = 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
        # Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m

def get_fibonacci_huge_fast(n, m):
# Write your code here
    Pisanoperiod = pisanoPeriod(m)
    n = n % Pisanoperiod
    previous = 0
    current = 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current \
        = current, previous + current   
    return (current % m)
   
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))

