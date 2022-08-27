# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return 1
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n-1)

def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n - 1)

print(factorial(12))

# uncomment when you're ready to test
print(sum_to_one(7))

