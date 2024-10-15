# Example file for Advanced Python by Joe Marini
# Formatting output strings

# Basic formatting - center(), ljust(), rjust()
# print("center".center(40, '-'))
# print("left".ljust(40, '.'))
# print("right".rjust(40, '.'))

val1 = 1234.5678
val2 = 10987.65
val3 = 12.99
val4 = -280.7

# Formatting strings with format specification codes
# Format spec is: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["."precision][type]
print(f"{val1}")
print(f"{val2}")
print(f"{val3}")
print(f"{val4}")

# Specify a precision


# Use alignment and width and leading zeros


# Use a grouping option and +/- signs


# Insert a fill character


# Create format specifiers dynamically
width = 10
precision = 2
format_spec = f"{123.456:{width}.{precision}f}"
print(format_spec)
format_spec = "{val:{width}.{precision}f}".format(val=val2,width=10,precision=2)
print(format_spec)
