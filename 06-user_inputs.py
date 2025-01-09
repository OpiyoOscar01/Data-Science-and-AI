while True:
  name=input("Enter your name: ")
  if(name.lower()=="exit"):
    print("Goodbye!")
    break
  else:
    age=input("Enter your age: ")
    height=input("Enter your height: ")
    print("Your name is "+name+" and you age is "+age+" years old,height is "+height)
   