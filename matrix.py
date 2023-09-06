def count_zeros(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element == 0:
                count += 1
    return count

# Example matrix
matrix = [
    [1, 0, 2],
    [0, 3, 4],
    [5, 0, 6]
]

zeros_count = count_zeros(matrix)
print("Number of zeros in the matrix:", zeros_count)
