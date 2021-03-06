#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring
# pylint: disable = unidiomatic-typecheck

# ------------
# Operators.py
# ------------

# https://docs.python.org/3/library/operator.html
# https://graphics.stanford.edu/~seander/bithacks.html

from copy     import copy, deepcopy
from operator import add

def test1 () :
    i = 2
    j = -i         # negation
    assert i ==  2
    assert j == -2

def test2 () :
    i = 2
    j = 3
    k = i + j     # addition
    assert i == 2
    assert j == 3
    assert k == 5

def test3 () :
    i = 2
    j = 3
    k = add(i, j) # addition
    assert i == 2
    assert j == 3
    assert k == 5

def test4 () :
    i = 2
    j = 3
    i += j        # in-place addition
    assert i == 5
    assert j == 3

def test5 () :
    i = 4
    j = 2
    f = i / j               # true division
    assert i == 4
    assert j == 2
    assert type(f) is float
    assert f == 2.0

def test6 () :
    i = 5
    j = 2
    k = i // j            # floor division
    assert i == 5
    assert j == 2
    assert type(k) is int
    assert k == 2

def test7 () :
    f = 5.0
    j = 2
    g = f // j              # floor division
    assert f == 5.0
    assert j == 2
    assert type(g) is float
    assert g == 2.0

def test8 () :
    i = 5
    j = 2
    k = i % j     # mod
    assert i == 5
    assert j == 2
    assert k == 1

def test9 () :
    i = 5
    j = 2
    i %= j        # in-place mod
    assert i == 1
    assert j == 2

def test10 () :
    i = 2
    j = 3
    k = i ** j    # exponentiation
    assert i == 2
    assert j == 3
    assert k == 8

def test11 () :
    i = 2
    j = 3
    i **= j       # in-place exponentiation
    assert i == 8
    assert j == 3

def test12 () :
    i = 2
    j = ~i         # bit complement
    k = ~j
    assert i ==  2
    assert j == -3
    assert k ==  2

def test13 () :
    i = 2
    j = 3
    k = i << j     # bit shift left
    assert i ==  2
    assert j ==  3
    assert k == 16

def test14 () :
    i = 2
    j = 3
    i <<= j        # in-place bit shift left
    assert i == 16
    assert j ==  3

def test15 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i & j      # 1000: bit and
    assert i == 10
    assert j == 12
    assert k ==  8

def test16 () :
    i = 10
    j = 12
    i &= j         # in-place bit and
    assert i ==  8
    assert j == 12

def test17 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i | j      # 1110: bit or
    assert i == 10
    assert j == 12
    assert k == 14

def test18 () :
    i = 10
    j = 12
    i |= j         # in-place bit or
    assert i == 14
    assert j == 12

def test19 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i ^ j      # 0110: bit exclusive or
    assert i == 10
    assert j == 12
    assert k ==  6

def test20 () :
    i = 10
    j = 12
    i ^= j         # in-place bit exclusive or
    assert i ==  6
    assert j == 12

def test21 () :
    i = 10
    j = 12
    i ^= j
    j ^= i
    i ^= j
    assert i == 12
    assert j == 10

def test22 () :
    a = True
    b = True
    c = False
    assert a and b
    assert not (a and c)
    assert a or b
    assert a or c

def test23 () :
    s = "abc"
    assert s[1] == "b" # str index
    #s[1] = "d"        # TypeError: 'str' object does not support item assignment

def test24 () :
    a = [2, 3, 4]
    assert a[1] == 3 # list index
    a[1] = 5
    assert a[1] == 5

def test25 () :
    u = (2, 3, 4)
    assert u[1] == 3 # tuple index
    #u[1] = 5        # TypeError: 'tuple' object does not support item assignment

def test26 () :
    a = [2, 3, 4]
    assert a[1]     == 3          # list slicing
    assert a[-1]    == 4
    assert a[1:2]   == [3]
    assert a[1:3]   == [3, 4]
    assert a[0:3]   == [2, 3, 4]
    assert a[0:3:2] == [2, 4]
    assert a[:]     == [2, 3, 4]

def test27 () :
    a = [2, 3, 4]
    b = a[:]
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a[1] == 3
    assert b[1] == 4

def test28 () :
    u = (2, 3, 4)
    v = u[:]
    assert u is v

def test29 () :
    a = [2, 3, 4]
    b = copy(a)
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a[1] == 3
    assert b[1] == 4

def test30 () :
    u = (2, 3, 4)
    v = copy(u)
    assert u is v

def test31 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = b[:]
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test32 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = copy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test33 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = deepcopy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is not c[1]
    assert b[1] ==     c[1]

def test34 () :
    s = "a"
    t = "bc"
    u = s + t             # string concatenation
    assert u is not "abc"
    assert u ==     "abc"

def test35 () :
    a = [2]
    b = [3, 4]
    c = a + b                 # list concatenation
    assert c is not [2, 3, 4]
    assert c ==     [2, 3, 4]
    assert c !=     (2, 3, 4)

def test36 () :
    u = (2,)
    v = (3, 4)
    w = (u + v)               # tuple concatenation
    assert w is not (2, 3, 4)
    assert w ==     (2, 3, 4)
    assert w !=     [2, 3, 4]

def test37 () :
    s = "abc"
    t = 2 * s                # string replication
    assert t is not "abcabc"
    assert t ==     "abcabc"

def test38 () :
    a = [2, 3, 4]
    b = 2 * a                          # list replication
    assert b is not [2, 3, 4, 2, 3, 4]
    assert b ==     [2, 3, 4, 2, 3, 4]

def test39 () :
    u = (2, 3, 4)
    v = 2 * u                          # tuple replication
    assert u is not (2, 3, 4, 2, 3, 4)
    assert v ==     (2, 3, 4, 2, 3, 4)

def test40 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += [5]
    assert a == [2, 3, 4, 5]
    assert a is b

def test41 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += (5,)
    assert a == [2, 3, 4, 5]
    assert a is b

def test42 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b = b + [5]
    assert a == [2, 3, 4]
    assert b == [2, 3, 4, 5]

def test43 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    #b = b + (5,) # TypeError: can only concatenate list (not "tuple") to list

def test44 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y += (5,)
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5)

def test45 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v += [5]     # TypeError: can only concatenate tuple (not "list") to tuple

def test46 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y = y + (5,)
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5)

def test47 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v = v + [5]  # TypeError: can only concatenate tuple (not "list") to tuple

def test48 () :
    i = 3
    j = 5
    k = 7
    l = 8
    assert (i < j) and (j < k) and (k < l)
    assert i < j < k < l

def test49 () :
    i = 10
    j = 12
    i, j = j, i
    assert i == 12
    assert j == 10

def test50 () :
    a = [2, 3]
    i, j = a
    assert i == 2
    assert j == 3

def main () :
    print("Operators.py")
    for i in range(50) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
