def fibcalls(n, count = 1):
    """ Computes the number of function calls to fib() required
        to compute the n-th Fibonacci number."""
    if n==1 or n==2:
        return count
    return fibcalls(n-1, count)+fibcalls(n-2, count)+1
