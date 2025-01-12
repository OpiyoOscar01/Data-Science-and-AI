# Variable scope is used to determine the region in which the variable can be accessed.
name="Opiyo Oscar-Global" #Accessible globally.
def greeting():
  # name="Opiyo Oscar-Local" #Accessible within the function only
  print("Hello "+name)

greeting()