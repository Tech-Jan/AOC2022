#!/usr/bin/env python
# not my solve
import sys
from itertools import zip_longest


def main() -> None:
    def compare(l, r) -> bool:
        myname=list(zip_longest(l, r, fillvalue=None))
        for ll, rr in zip_longest(l, r, fillvalue=None):
            if ll == None: return True
            if rr == None: return False
            instancell=isinstance(ll, int)
            instancerr=isinstance(rr, int)
            if isinstance(ll, int) and isinstance(rr, int):
                if ll > rr: return False
                if ll < rr: return True
            else:
                if isinstance(rr, int): rr = [rr]
                if isinstance(ll, int): ll = [ll]

                ret = compare(ll, rr)
                if ret in [True, False]: return ret
                else: print("WTFF")

    itxt = open("../input/input", mode='r').read().split("\n\n")
    itxt = [i.splitlines() for i in itxt]

    pkts = [eval(j) for i in itxt for j in i]
    pkts = [[list(pl), list(pr)] for pl, pr in zip(pkts[0::2], pkts[1::2])]

    out = [i for i, p in enumerate(pkts, 1) if compare(*p) == True]
    print(out)


if __name__ == '__main__':
    sys.exit(main())