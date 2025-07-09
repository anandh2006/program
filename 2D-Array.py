# Ask how many rows the array should have
rows = int(input("Enter number of rows: "))

# Create an empty list to hold the 2D array
arr = []

# Loop through each row
for i in range(rows):
    # Ask how many columns for this row
    cols = int(input(f"Enter number of columns for row {i + 1}: "))

    # Ask for that many numbers (space-separated)
    row_input = input(f"Enter {cols} numbers for row {i + 1}, separated by space: ")

    # Convert the input string into a list of integers
    row = list(map(int, row_input.split()))

    # Add the row to the main array
    arr.append(row)

# Print the 2D array
print("\nThe 2D array is:")
for row in arr:
    for num in row:
        print(num, end=" ")
    print()  # Newline after each row
