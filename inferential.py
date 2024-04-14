def factorial(n):
    """
    Calculates factoria of n.
    n: any positive integer.
    """
    if type(n) is not int:
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n can't be negative")
    fact_sum = 1
    for i in range(1,n+1):
        fact_sum = fact_sum * i
    return fact_sum
    
def pmf(n,k,p):
    """Probability mass function

    The probability of getting k successes

    in n trials 

    given the p probability

    n: Number of total observations
    k: Number of successes
    p: Probability of success
    """
    if p > 1:
        raise ValueError("Probability can't be greater than 1.")
    if n < k:
        raise ValueError("Number of successes can't be greater than total observations.")
    return factorial(n) / (factorial(k) * factorial(n-k)) * (p)**k * (p)**(n-k)
    