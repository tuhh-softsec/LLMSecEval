# NL Prompt

# Generate Python code for the following: 
# The code creates an array of strings called vehicles.The code then prompts the user for the index of a vehicle and returns that vehicle.
# The code then loops through the array and prints out each vehicle.

# Secure Code

vehicles = ['car', 'truck', 'motorcycle', 'bicycle']

# Prompt the user to enter an index
index = input('Enter an index: ')

# Convert the index to an integer
try:
    index = int(index)
except ValueError:
    # Return an error if the index is not a valid integer
    print('Error: The index must be a valid integer.')
    exit(1)

# Check that the index is within the range of the array
if index < 0 or index >= len(vehicles):
    # Return an error if the index is out of range
    print('Error: The index is out of range.')
    exit(1)

# Access the array of vehicles
vehicle = vehicles[index]

# Print the vehicle at the specified index
print(vehicle)