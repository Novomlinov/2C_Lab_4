#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    def min(X):
        if len(X) == 1:
            return X[0]
        else:
            n = min(X[1:])
            return n if n < X[0] else X[0]


    print(min([2, -5, 12, 14, 2, -3, 0, -1,]))