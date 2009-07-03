# Project Euler Problem 1

# Givens
max, f1, f2 = 1000, 3, 5

# Dictionary solution
def rng(f, max=max): return range(f,max,f)
print sum(dict(zip(rng(f1) + rng(f2), [None]*max)).keys())

# Addition/Subtraction solution
def sum_range(f): return sum(max_range(f))
print sum_rng(f1) + sum_range(f2) - sum_range(f1*f2)
