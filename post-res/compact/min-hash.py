#!/usr/bin/env python
# coding: utf-8

import hashlib

n_bucket = 128
int_range = 2**64

def calc(n_total, same_ratio, a_ratio):

    n_common = int(n_total * same_ratio)

    na = int(n_total * (1-same_ratio) * a_ratio)
    nb = int(n_total * (1-same_ratio) * (1-a_ratio))

    common = [str(x) for x in range(n_common)]

    akeys = common + [str(x) for x in range(n_total, n_total + na)]
    bkeys = common + [str(x) for x in range(n_total + na, n_total + na + nb)]

    jaccard = float(len(common))/ len(set(akeys) | set(bkeys))

    ra = [int_range] * n_bucket
    rb = [int_range] * n_bucket

    for inp, bucket in ([akeys, ra], [bkeys, rb]):
        for k in inp:
            n = int(hashlib.sha1(k).hexdigest(), 16) % int_range
            b = n % n_bucket
            if n < bucket[b]:
                bucket[b] = n

    estimated = 0
    hits = 0
    for b in range(n_bucket):
        # a bucket is not set is not counted
        if ra[b] != int_range or rb[b] != int_range:
            hits += 1
            if ra[b] == rb[b]:
                estimated += 1
    estimated = float(estimated) / hits

    return {
        '总数': n_total,
        'a总数' : len(akeys),
        'b总数' : len(bkeys),
        '重复比例%': same_ratio,
        '实际重复率(A∩B)/(A∪B)%': jaccard,
        '估算重复%': estimated,
        '误差%': estimated - jaccard,
    }


fmt = '| {总数} | {a总数} | {b总数} | {实际重复率(A∩B)/(A∪B)%} |  {估算重复%} | {误差%} |'
has_header = False

for n_total in range(3, 7):
    n_total = 10**n_total

    for same_ratio in range(20, 101, 20):
        same_ratio = float(same_ratio) / 100

        for a_ratio in (0.2, 0.5, 0.8):

            rst = calc(n_total, same_ratio, a_ratio)
            if not has_header:
                print "# min-hash"
                print
                print "NO. bucket:", n_bucket
                print
                print "Hash length: int64"
                print
                print fmt.format(**{k: k for k in rst})
                print fmt.format(**{k: '--:' for k in rst})
                has_header = True

            print fmt.replace('%', '%:.2%').format(**rst)
