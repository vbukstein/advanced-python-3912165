# Example file for Advanced Python by Joe Marini
# Understanding Python scope


# declare a variable within the global scope
x=1


# define a local function with a variable "x"
def test():
  x=10
  print(x)

# Run the test function and observe the two results
test()
print(x)

x=x+5
print(x)
test()

# Nested functions create inner scopes. These are called closures:
