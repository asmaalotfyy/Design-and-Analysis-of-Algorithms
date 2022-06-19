# Uses python3
import numpy as np


def split(array):

    row, col = array.shape
    row2, col2 = row//2, col//2
    return array[:row2, :col2], array[:row2, col2:], array[row2:, :col2], array[row2:, col2:] 


def ConquerMatrix(q1, q2, q3, q4, nq): # Merge the divided four small matrices into one large matrix.

    result = [[0 for _ in range(2*nq)]
                 for _ in range(2*nq)]

    for i in range(2*nq):
        for j in range(2*nq):
            if (i < nq):
                if (j < nq):
                    result[i][j] = q1[i][j]
                else:
                    result[i][j] = q2[i][j-nq]
            else:
                if (j < nq):
                    result[i][j] = q3[i-nq][j]
                else:
                    result[i][j] = q4[i-nq][j-nq]

    return result

def matrix_mult_fast(A, B, n):
    # Write your BONUS code here
     if n == 0:
        return [[]]

     elif n == 1:
          product = A * B
          return product
     elif n > 1:
        a1, a2, a3, a4 = split(A)
        b1, b2, b3, b4 = split(B)
        row, col = a1.shape
        n = row
        r1 = matrix_mult_fast(a1,b2 - b4,n) 
        r2 = matrix_mult_fast(a1 + a2,b4,n)       
        r3 = matrix_mult_fast(a3 + a4,b1,n)       
        r4 = matrix_mult_fast(a4,b3 - b1,n)       
        r5 = matrix_mult_fast(a1 + a4,b1 + b4,n)       
        r6 = matrix_mult_fast(a2 - a4,b3 + b4,n) 
        r7 = matrix_mult_fast(a1 - a3,b1 + b2,n) 
        r1, r2, r3, r4 ,r5, r6, r7 = np.array(r1), np.array(r2), np.array(r3), np.array(r4), np.array(r5), np.array(r6), np.array(r7)

        c1 = r5 + r4 - r2 + r6
        c2 = r1 + r2          
        c3 = r3 + r4           
        c4 = r1 + r5 - r3 - r7 
        
        product = ConquerMatrix(c1,c2,c3,c4,n)
        
        return product
 

def matrix_mult(A, B, n):
    
# Write your code here
    if n == 0:
        return [[]]

    elif n == 1:
        product = A * B
        return product
    elif n > 1:
        a1, a2, a3, a4 = split(A)
        b1, b2, b3, b4 = split(B)
        row, col = a1.shape
        n = row
       
        c1 = np.array(matrix_mult(a1,b1,n)) + np.array(matrix_mult(a2,b3,n))
        c2 = np.array(matrix_mult(a1,b2,n)) + np.array(matrix_mult(a2,b4,n))
        c3 = np.array(matrix_mult(a3,b1,n)) + np.array(matrix_mult(a4,b3,n))
        c4 = np.array(matrix_mult(a3,b2,n)) + np.array(matrix_mult(a4,b4,n))

        product = ConquerMatrix(c1,c2,c3,c4,n)

        return product


if __name__ == '__main__':
    n = int(input())
    A = []
    B = []
    # Enter matrix 1 values, press enter after each row
    # Matrix 1 filling
    for i in range(n):
        A.append([int(j) for j in input().split()]) 

    # Enter matrix 2 values, press enter after each row
    # Matrix 2 filling
    for i in range(n):
        B.append([int(j) for j in input().split()]) 

    # A = np.array(A)
    # B = np.array(B)
    
    # A = [[ 1 , 2 , 3 , 4]
    #     [ 5 , 6 , 7 , 8]
    #     [ 9 , 10 , 11 , 12]
    #     [13 , 14 , 15 ,  16]]
    # B = [[ 1 , 2 , 3 , 4]
    #     [ 5 , 6 , 7 , 8]
    #     [ 9 , 10 , 11 , 12]
    #     [13 , 14 , 15 ,  16]]
    
    A = np.array(A)
    B = np.array(B)

    # a1, a2, a3, a4 = split(A)
    # b1, b2, b3, b4 = split(B)
    # row, col = A.shape
    print(A)
    # print(a4 * b4)
    
    print(matrix_mult(A, B, n))
    print("------------------------------------------")
    ''' UNCOMMENT this line if you will submit BONUS'''
    print(matrix_mult_fast(A, B, n))