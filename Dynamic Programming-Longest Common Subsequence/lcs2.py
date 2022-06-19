#Uses python3
import sys

def lcs2(a, b):
    #write your code here
     c   = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)] 
     for i in range(1, len(a) + 1):
        c[0][i] = 0
     for j in range(1, len(b) + 1):
        c[j][0] = 0

     for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):

            if a[i - 1] == b[j - 1]:
                c[j][i] = max(c[j - 1][i - 1] + 1, c[j][i - 1], c[j - 1][i])
            else:
                c[j][i] = max(c[j - 1][i - 1], c[j][i - 1], c[j - 1][i])

     return c[len(b)][len(a)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
