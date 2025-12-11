# Nuri Zilvani
# D0425008


# Array 1 Dimensi
array_1d = [11, 12, 13, 14, 15]
print("Array 1D:", array_1d)

# Array 2 Dimensi 
array_2d = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
print("Array 2D:")
for row in array_2d:
    print(row)

# Array 3 Dimensi
array_3d = [
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]],
    [[13, 14], [15, 16]]
]
print("\nArray 3D:")
for i, layer in enumerate(array_3d):
    print(f"Layer {i}: {layer}")