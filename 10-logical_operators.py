# Logical operators(and,or ,not) are used to check of one or more conditional statements are true or false.
temperature=float(input("Enter the temperature today:"))
if temperature>0 and temperature<30:
  print("The temperature is good today.Go outside")
elif temperature<0 or temperature>30:
  print("The temperature is bad today.Stay inside")
else:
  print('Invalid input')
  
# The use of not logical operator
if not(temperature>0 and temperature<30):
  print("The temperature is bad today.Stay inside")

  