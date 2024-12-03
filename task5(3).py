#USING PYTHON LAMBDA FUNCTION TO CREATE A FIBNACCI SERIES FROM 1 TO 50
fib = lambda n:n if n<2 else fib(n-1) +fib(n-2)
fib_series = [fib(n) for n in range(1,51)]
print(fib_series)