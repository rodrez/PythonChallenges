n = 20
temp = n

# Loops that creates the pyramid like text object
for i in range(1,n+1):
  print(" " * temp, '#' * i, end='')
  print("  ", end="")
  print("#" * i)
  temp -= 1
