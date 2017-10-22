#!/usr/bin/env python2.6
# coding: utf-8

import sys
import math
import time
import hashlib

def normal_pdf(x, mu, sigma):
    x = float(x)
    mu = float(mu)

    m = 1.0 / math.sqrt( 2 * math.pi ) / sigma
    n = math.exp(-(x-mu)**2 / (2*sigma*sigma))

    return m * n

def normal_cdf(x, mu, sigma):
    # integral(-oo,x)

    x = float(x)
    mu = float(mu)
    sigma = float(sigma)

    # to standard form
    x = (x - mu) / sigma

    s = x
    v = x
    for i in range(1, 100):
        v = v * x * x / (2*i+1)
        s += v

    return 0.5 + s/(2*math.pi)**0.5 * math.e ** (-x*x/2)

def difference(nbucket, nkey):

    nbucket, nkey= int(nbucket), int(nkey)

    # binomial distribution approximation by normal distribution
    # find the bucket with minimal keys.
    #
    # the probability that a bucket has exactly i keys is:
    #   # probability density function
    #   normal_pdf(i, mu, sigma)
    #
    # the probability that a bucket has 0 ~ i keys is:
    #   # cumulative distribution function
    #   normal_cdf(i, mu, sigma)
    #
    # if the probability that a bucket has 0 ~ i keys is greater than 1/nbucket, we
    # say there will be a bucket in hash table has:
    # (i_0*p_0 + i_1*p_1 + ...)/(p_0 + p_1 + ..) keys.
    p = 1.0 / nbucket
    mu = nkey * p
    sigma = math.sqrt(nkey * p * (1-p))

    target = 1.0 / nbucket
    minimal = mu
    while True:

        xx = normal_cdf(minimal, mu, sigma)
        if abs(xx-target) < target/10:
            break

        minimal -= 1

    return minimal, (mu-minimal) * 2 / (mu + (mu - minimal))

def difference_simulation(nbucket, nkey):

    t = str(time.time())
    nbucket, nkey= int(nbucket), int(nkey)

    buckets = [0] * nbucket

    for i in range(nkey):
        hsh = hashlib.sha1(t + str(i)).digest()
        buckets[hash(hsh) % nbucket] += 1

    buckets.sort()
    nmin, mmax = buckets[0], buckets[-1]

    return nmin, float(mmax - nmin) / mmax

if __name__ == "__main__":

    bks = range(2, 7)
    print '| <sub>b</sub>\<sup>n</sup>',
    for bk in bks:
        print ' | 10^' + str(bk),
    print

    for b in (100, 1000, 10000):
        print '|', b,
        for bk in bks:
            bk = 10**bk
            r = difference(b, b*bk)[1]
            r = ' | {r:.1%}'.format(r=r)
            print r,
        print ' |'

    raise


    nbucket, nkey= sys.argv[1:]

    minimal, rate = difference(nbucket, nkey)
    print 'by normal distribution:'
    print '     min_bucket:', minimal
    print '     difference:', rate

    minimal, rate = difference_simulation(nbucket, nkey)
    print 'by simulation:'
    print '     min_bucket:', minimal
    print '     difference:', rate
