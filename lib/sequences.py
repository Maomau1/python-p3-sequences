#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    fibonacci = []
    if length == 1 :
        fibonacci = [0]
    elif length ==2 :
        fibonacci = [0,1]
    elif length > 2 :
        fibonacci = [0,1]
        i=1
        while i < length -1 :
            fibonacci.append(fibonacci[i]+fibonacci[i-1])
            i+=1
    print(fibonacci)
    