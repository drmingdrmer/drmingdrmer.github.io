#!/usr/bin/env python
# coding: utf-8

import sys
import hashlib
import math

def make_buckets(nbucket, nkey):
    buckets = [0] * nbucket

    for i in range(nkey):
        hsh = hashlib.sha1(str(i)).digest()
        buckets[hash(hsh) % nbucket] += 1

    buckets.sort()
    return buckets

def uniformity(nbucket, nkey, nlines=20):

    avg = nkey / nbucket

    nb = nbucket / nlines

    buckets = make_buckets(nbucket, nkey)
    for i in range(nlines):
        n = sum(buckets[i*nb : i*nb+nb]) / nb
        print '%02.2f%%' % ( float(n*100) / avg )

if __name__ == "__main__":
    b, k = sys.argv[1:]
    b, k = int(b), int(k)
    uniformity( b, k)
