#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(maxlim: int) -> int:
    a, b = 0, 1
    while a < maxlim:
        a, b = b, a + b
        yield a

def sum_even_fib() -> int:
    sum1 = 0
    for i in fib(4_000_000):
        if i % 2 == 0:
            sum1 += i
    return sum1


def main():
    print(f"result={sum_even_fib()}")

if __name__ == '__main__':
    main()
