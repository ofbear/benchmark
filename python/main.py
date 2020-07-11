#!/usr/bin/python3.6
def fib(n):
    if n < 2:
        return n

    return fib(n - 2) + fib(n - 1)

print(f"{fib(38)}")
