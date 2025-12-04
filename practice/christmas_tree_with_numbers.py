
def draw_christmas_tree(height):
    """
    This function draws a Christmas tree with numbers.

    Args:
        height: The height of the tree.
    """
    # Draw the tree
    for i in range(1, height + 1):
        # Print spaces
        for j in range(height - i):
            print(" ", end="")
        # Print numbers
        for k in range(2 * i - 1):
            print(i, end="")
        # print()

    # Draw the trunk
    for i in range(2):
        for j in range(height - 1):
            print(" ", end="")
        print("|")

if __name__ == "__main__"
    tree_height = 5
    draw_christmas_tree(tree_height)
