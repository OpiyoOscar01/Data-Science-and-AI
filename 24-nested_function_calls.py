# Nested function calls in Python
# This is a simple example of nested function calls in Python

def outer_function():
    print("Inside outer_function")
    
    def inner_function():
        print("Inside inner_function")

outer_function()

print(round(abs(float(input("Enter a number: ")))))