"""Finite *sanity check*, not proof: sharp multipartite theorem, n <= 21.

Enumerates unordered nonempty class-size partitions and each integer d with
2 <= d <= n/2. Checks sharp-edge inequality and equality classification
using exact rational numbers and the paper's closed-form cycle spectra.
"""
from fractions import Fraction


def partitions(n, lower=1):
    if n == 0:
        yield ()
        return
    for k in range(lower, n + 1):
        for tail in partitions(n - k, k):
            yield (k,) + tail


def H(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction())


def run(max_n=21):
    examined = 0
    for n in range(4, max_n + 1):
        for classes in partitions(n):
            if len(classes) < 2:
                continue
            r = len(classes)
            s = n - max(classes)
            e = (n * n - sum(a * a for a in classes)) // 2
            value = (H(s) - 1) / 2 if r == 2 else H(min(n, 2 * s)) - Fraction(3, 2)
            for d in range(2, n // 2 + 1):
                if e <= (d - 1) * (n - d + 1):
                    continue
                examined += 1
                bound = (H(d) - 1) / 2
                assert value >= bound, (n, classes, d, e, value, bound)
                equality = r == 2 and s == d
                assert (value == bound) == equality, (n, classes, d, e, value)
    print(f'Multipartite tests: {examined:,}; violations: 0; max order: {max_n}')


if __name__ == '__main__':
    run()
