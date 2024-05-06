import math

# Function to convert degrees to radians and return as a symbolic fraction of pi if possible
def convert_degrees_to_radians_symbolic(degrees):
    # Convert degrees to radians
    radians = degrees * (math.pi / 180)
    # Check if the radians can be expressed as a fraction of pi
    for denominator in range(1, 9):  # Limit the denominator to 8 for simplicity
        fraction = math.pi / denominator
        if math.isclose(radians, fraction, rel_tol=1e-9):
            return f"π/{denominator}"
    return radians

# Convert 45 degrees to radians and display as a fraction of pi if possible
radians_symbolic = convert_degrees_to_radians_symbolic(60)

print(radians_symbolic)
