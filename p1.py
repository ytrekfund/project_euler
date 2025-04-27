#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_fators(n: int) -> int:
    sum1 = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            sum1 += i
    return sum1

def main():
    print(f"result={sum_fators(1000)}")

if __name__ == '__main__':
    main()
