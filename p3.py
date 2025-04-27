#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_max_fators(n: int) -> int:
    maxfac = 0
    fac = 2
    while fac <= n:
        if n % fac == 0:
            n /= fac
            maxfac = fac
        else:
            fac += 1
    return maxfac

def main():
    print(f"result={get_max_fators(60085_1475143)}")

if __name__ == '__main__':
    main()
