"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(x: float, y: float):
    return x * y


def id(x: float):
    return x


def add(x: float, y: float):
    return x + y


def neg(x: float):
    return -x


def lt(x: float, y: float):
    return 1.0 if x < y else 0.0


def eq(x: float, y: float):
    return 1.0 if x == y else 0.0


def max(x: float, y: float):
    return x if x > y else y


def is_close(x: float, y: float) -> bool:
    return abs(x - y) < 1e-2


def sigmoid(x: float):
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    exp_x = math.exp(x)
    return exp_x / (1.0 + exp_x)


def relu(x: float):
    return x if x > 0 else 0.0


def log(x: float):
    return math.log(x)


def exp(x: float):
    return math.exp(x)


def inv(x: float):
    return 1.0 / x


def log_back(x: float, d: float):
    return d / x


def inv_back(x: float, d: float):
    return -d / (x * x)


def relu_back(x: float, d: float):
    return d if x > 0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(func):
    def map_function(iter: Iterable):
        ans = []
        for i in iter:
            ans.append(func(i))
        return ans
    return map_function

def zipWith(func):
    def zip_function(x: Iterable, y: Iterable):
        c = []
        for a, b in zip(x, y):
            c.append(func(a, b))
        return c
    return zip_function

def reduce(func, start):
    def reduce_function(iter: Iterable):
        acc = start
        for i in iter:
            acc = func(acc, i)
        return acc
    return reduce_function

def negList(iter):
    return map(neg)(iter)

def addLists(x, y):
    return zipWith(add)(x, y)

def sum(iter):
    return reduce(add, 0.0)(iter)

def prod(iter):
    return reduce(mul, 1.0)(iter)
