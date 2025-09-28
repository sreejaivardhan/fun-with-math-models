# Fun With Math Models
# Author: Jeetu (sreejaivardhan)

import math

def fibonacci(n):
    """Return first n Fibonacci numbers"""
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def prime_numbers(n):
    """Return first n prime numbers"""
    primes = []
    num = 2
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def circle_area(radius):
    """Return area of a circle"""
    return math.pi * radius * radius

def triangle_area(base, height):
    """Return area of a triangle"""
    return 0.5 * base * height

if __name__ == "__main__":
    print("=== Fun With Math Models ===")
    print("First 10 Fibonacci numbers:", fibonacci(10))
    print("First 10 Prime numbers:", prime_numbers(10))
    print("Area of circle with radius 5:", circle_area(5))
    print("Area of triangle with base 6 and height 4:", triangle_area(6, 4))
