import numpy as np

# Access point coordinates
AP1 = np.array([0, 0])
AP2 = np.array([0, 10])
AP3 = np.array([10, 0])

# RSSI values (in dB)
r1 = -60
r2 = -70
r3 = -80

# Distance calculation based on RSSI value (you need to calibrate this based on your own setup)
def calculate_distance(rssi, a=-45, n=2):
    return 10**((a - rssi) / (10 * n))

# Calculate the distances from the access points to the device
d1 = calculate_distance(r1)
d2 = calculate_distance(r2)
d3 = calculate_distance(r3)

# Trilateration calculation
A = 2 * np.array([AP2 - AP1, AP3 - AP1])
b = np.array([d1**2 - d2**2 - AP1[0]**2 + AP2[0]**2 - AP1[1]**2 + AP2[1]**2,
              d1**2 - d3**2 - AP1[0]**2 + AP3[0]**2 - AP1[1]**2 + AP3[1]**2])
x, y = np.linalg.solve(A, b)

# Print the calculated position
print("Position: ({}, {})".format(x, y))
