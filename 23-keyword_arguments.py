# Key word arguments are used to pass a variable number of arguments to a function.
def greetUser(last_name,first_name,middle_name):
  print("Hello "+first_name+" "+middle_name+" "+last_name)

# positional arguments
greetUser("Opiyo","Oscar","John")

# keyword arguments
greetUser(first_name="Oscar",middle_name="John",last_name="Opiyo")