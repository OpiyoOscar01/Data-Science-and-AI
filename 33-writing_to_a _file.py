import os
text="\nHello Oscar.\nGood afternoon.\nYou are becoming an expert in Python.\nPlease keep it up!\n"
text2="\nAlways push your code to github."
try:
  with open("hello.txt",'a') as f:
    f.write(text2)
    print("File written to successfully.")
except FileNotFoundError as e:
  print("Error: {}".format(e))