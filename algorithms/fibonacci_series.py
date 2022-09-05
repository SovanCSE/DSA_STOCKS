############################################################################################
## Category: Dinamic Programming
## Title: Display fibonacci series
## Short notes -
##   Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) while n >=2
## Example of the fibonacci series: 0 1 1 2 3 5
############################################################################################

## Solution without recursive way
a = 0
b = 1
sum_values = 0
for i in range(5):
    c = a
    sum_values += c
    print(f"number: {c}")
    a = b
    b = c + a
print('sum_values = ', sum_values)

##Solution with recurvise way
def fibonacci(num):

    if num < 0:
        return ("Incorrect input")

    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print('sum values(with recursion)', fibonacci(5))