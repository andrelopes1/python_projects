# Replace the old syntax with the with statement
with open('fun_file.txt') as close_this_file:
    setup = close_this_file.readline()
    punchline = close_this_file.readline()

# The file will automatically close when we exit the with block
print(setup)
