from sympy import isprime
print(list(filter(lambda x: isprime(x), range(10000))))
print([i for i in range(10000) if isprime(i)])  # I think it is The best way
