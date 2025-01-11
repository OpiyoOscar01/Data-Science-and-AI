# Nested loops are loops within loops.
# The inner loop will be executed one time for each iteration of the outer loop.
# Let's see an example:
for i in range(3):
  for j in range(3):
    print(i,j)
# The outer loop runs 3 times.
# The inner loop runs 3 times for each iteration of the outer loop.
name="Oscar Opiyo"
for letter in name:
  for i in range(3):
    print(letter,i)

rows=int(input("Enter the number of rows:"))
columns=int(input("Enter the number of columns:"))
symbol=input("Enter the symbol to use:")
for i in range(rows):
  for j in range(columns):
    print(symbol,end=" ")
  print()
  