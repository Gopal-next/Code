# Staircase ascending:

# *
# **
#   **
#   ***
#     ***
#     ****

blocks = 4
indent = 0

for block in range(1, blocks + 1):
    # first row of block
    print(" " * indent + "*" * block)
    # second row of block
    print(" " * indent + "*" * (block + 1))
    
    indent += 2  # increase indentation for next block



