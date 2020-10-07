#!/usr/bin/python3


def reverse(A):
    n = len(A)
    B = A.copy()
    for i in range(n):
        B[i] = A[(n-1)-i]
    return B


A = [1,2,3,4]
print(reverse(A))
