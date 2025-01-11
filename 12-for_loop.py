# for loop is a statement that allows you to execute a block of code a fixed number of times
# while loop is a statement that allows you to execute a block of code as long as its condition is true
import time
for i in range(5):
  print("Hello "+str(i))

for i in  range(50,100+1,10):
  print(i)

for letter in "Oscar Opiyo":
  print(letter)
  
for second in range(10,0,-1):
  print(second)
  time.sleep(1)
print("Happy New Year!")

