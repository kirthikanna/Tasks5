#USING PYTHON LAMBDA FUNCTION TO CREATE A FIBNACCI SERIES FROM 1 TO 50
fibonacci_series = []
a,b = 0,1
while b <= 50:
    fibonacci_series.append(b)
    a, b = b, (lambda x,y: x+y) (a,b)
print(fibonacci_series)

