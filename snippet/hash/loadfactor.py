#!/usr/bin/env python
# coding: utf-8

import math
import sys

pempty = lambda x: math.e ** (-x)
pone = lambda x: x * math.e ** (-x)
pcollision = lambda x: 1 - (1+x) * math.e ** (-x)
perc = lambda x: '%02.0f%%' % (x*100)

if __name__ == "__main__":
    loadfactors = [float(x) for x in sys.argv[1:]]
    for lf in loadfactors:
        print 'load factor: %02.2f,  empty: %s, 1-key: %s, collision: %s' % (
                lf,
                perc(pempty(lf)),
                perc(pone(lf)),
                perc(pcollision(lf)),
        )
