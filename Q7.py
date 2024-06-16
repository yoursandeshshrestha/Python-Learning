def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=", ")
        a, b = b, a + b

n = int(input("Enter the number: "))
print(f"Fibonacci series up to {n} terms:")
fibonacci_series(n)
