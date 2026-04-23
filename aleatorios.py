"""
Zuzanna Masklak

This file contains the class Aleat and the generator function aleat()
for pseudo-random number generation using the LCG method.
"""


class Aleat:
    """Iterator that generates pseudo-random numbers using the LCG method.

    The class implements a linear congruential generator (LCG) that produces
    numbers in the range 0 <= x_n < m.

    Attributes:
        m: Modulus of the generator.
        a: Multiplier of the generator.
        c: Increment of the generator.
        x: Current state of the sequence.

    Methods:
        __iter__():
            Returns the iterator itself.
        __next__():
            Computes and returns the next pseudo-random number.
        __call__(x0):
            Resets the sequence using x0 as the new seed.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0, /):
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Generator function that produces pseudo-random numbers using the LCG method.

    The function generates numbers in the range 0 <= x_n < m using the
    linear congruential formula. The parameters m, a, c, and x0 can be
    configured, and they have the same default values as in the Aleat class.

    Args:
        m: Modulus of the generator.
        a: Multiplier of the generator.
        c: Increment of the generator.
        x0: Initial seed of the sequence.

    Yields:
        The next pseudo-random number in the sequence.

    If a value is sent to the generator using send(), the sequence is
    restarted using that value as the new seed.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38

    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """

    x = x0
    while True:
        x = (a * x + c) % m
        new_seed = yield x
        if new_seed is not None:
            x = new_seed


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)