# Pascal's triangle with symbols:

    #           *
    #          * *
    #         *   *
    #        *  *  *
    #       *   *   *
    #      *  *   *  *
    #     *   *   *   *
    #    *  *   *   *  *
    #   *   *   *   *   *
    #  *  *   *   *   *  *
    # *   *   *   *   *   *

n = 14

for i in range(n):
    # Calculate number of stars: 1, 2, 2, 3, 3, 4, 4, 5, 5
    if i == 0:
        num_stars = 1
    else:
        num_stars = ((i + 1) // 2) + 1
    
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    
    # Print stars with spacing
    for j in range(num_stars):
        print("*", end="")
        if j < num_stars - 1:
            if i == 1:  # Row 1: 1 space
                print(" ", end="")
            elif i % 2 == 0:  # Even rows: all 3 spaces
                print("   ", end="")
            else:  # Odd rows (3, 5, 7...): edges 2, middle 3
                if j == 0 or j == num_stars - 2:  # first or last gap
                    print("  ", end="")
                else:
                    print("   ", end="")
    
    print()





# *
# **
# **
# ***
# ***
# ****
# ****
