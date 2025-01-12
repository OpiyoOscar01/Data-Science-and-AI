# Exception=an event that disrupts the normal execution of the program
"""
This script demonstrates basic exception handling in Python.
It prompts the user to input a numerator and a denominator, then attempts to divide the numerator by the denominator.
If the denominator is zero, a ZeroDivisionError is caught and an appropriate message is displayed.
If any other exception occurs, a generic error message is displayed.
Exceptions handled:
- ZeroDivisionError: Raised when attempting to divide by zero.
- Exception: Catches any other exception that is not specifically handled.
Other common exceptions in Python include:
- ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
- TypeError: Raised when an operation or function is applied to an object of inappropriate type.
- IndexError: Raised when a sequence subscript is out of range.
- KeyError: Raised when a dictionary key is not found.
- FileNotFoundError: Raised when a file or directory is requested but doesn't exist.
- IOError: Raised when an input/output operation fails.
- AttributeError: Raised when an attribute reference or assignment fails.
- ImportError: Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
"""
try:
  numerator=float(input("Enter the numerator"))
  denominator=float(input("Enter the denominator"))
  result=numerator/denominator
except ZeroDivisionError as e:
  print("Error:{error}".format(error=e))
  print("You can'r divide by zero!")
except ValueError as e:
  print("Error:{error}".format(error=e))
  print("Invalid input! Please enter numeric values.")
except Exception as e:
  print("Error:{error}".format(error=e))
  print("Something went wrong")
else:
        print("Result is {:.4f}".format(result))
finally:
  print("This is always executed")

  
  