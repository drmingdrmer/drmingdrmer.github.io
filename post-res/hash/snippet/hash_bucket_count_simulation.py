#!/usr/bin/env python
# coding: utf-8

import sys
import hashlib
import math

def count_collision(nbucket, nkey):

    buckets = [0] * nbucket

    for i in range(nkey):
        hsh = hashlib.sha1(str(i)).digest()
        buckets[hash(hsh) % nbucket] += 1

    buckets.sort()
    counter = {}

    for n in buckets:
        if n not in counter:
            counter[n] = 0

        counter[n] += 1

    for n, b in counter.items():
        print b, "buckets with", n, "keys", str(int(float(b)/nbucket*100)) + '%'

if __name__ == "__main__":
    b, k = sys.argv[1:]
    b, k = int(b), int(k)
    count_collision( b, k)
