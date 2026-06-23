# Function to generate the required shape
def generate_shape(n, shape):
    grid = []  # Stores the final NxN grid

    # Generate checkerboard pattern
    if shape == "checkerboard":
        for i in range(n):  # Loop through each row
            row = []

            for j in range(n):  # Loop through each column
                # Alternate between 0 and 1
                row.append((i + j) % 2)

            grid.append(row)  # Add completed row to grid

    # Generate diamond pattern
    elif shape == "diamond":
        mid = n // 2  # Find the center of the grid

        for i in range(n):  # Loop through rows
            row = []

            for j in range(n):  # Loop through columns

                # Check if the current cell lies inside the diamond
                if abs(i - mid) + abs(j - mid) <= mid:
                    row.append(1)
                else:
                    row.append(0)

            grid.append(row)  # Add row to grid

    return grid  # Return the completed shape


# Take grid size as input
n = int(input())

# Take shape name as input ("checkerboard" or "diamond")
shape = input()

# Validate the grid size
if 5 <= n <= 51:

    # Generate the requested shape
    result = generate_shape(n, shape)

    # Print the grid row by row
    for row in result:
        print(*row)

else:
    print("Invalid N")