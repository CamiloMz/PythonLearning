# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 20:
    # print(a, end=',') The keyword argument end can be used to avoid the newline after the output, or end the output with a different string
    print(a)
    a, b = b, a+b


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)