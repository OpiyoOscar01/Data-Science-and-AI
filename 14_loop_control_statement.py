# Loop control statement is a statement that allows you to control the flow of a loop
# Loop control statements are:
# 1. break statement is used to terminate the loop entirely
# 2. continue statement used to skip the current block and return to the loop
# 3. pass statement is used to do nothing
# example of break statement
name='Oscar'
for letter in name:
  if letter=='a':
    break
  print(letter,end="")
print()
# example of continue statement
for letter in name:
  if letter=='a':
    continue
  print(letter,end="")
print()
phone_number ="+256756-697-871"
for i in phone_number:
  if i=='-' or i=='+':
    continue
  print(i,end="")
print()
# example of pass statement
for letter in name:
  if letter=='a':
    pass
  print(letter,end="")
print()

