# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(5))
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
XFTW-NNKQ
fibonacci_runtime = "2^N"