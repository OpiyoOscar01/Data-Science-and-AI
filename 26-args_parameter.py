# *args parameter is used so we can pass varying number of parameters to a function as a tuple.

def add(*values):
  sum =0;
  for value in values:
    sum+=value
  return sum

sum=add(12,34,87)
print(sum)
sum2=add(23,47,9,23,67,23)
print(sum2)
