"""
Assignment 2: Fractal Generator

Author: Rie Pilgaard Christiansen

Description:
This script generates fractal patterns using recursive functions and geometric transformations.
"""

# Importing libraries for plotting and geometry manipulation
import matplotlib.pyplot as plt
import numpy as np
import random
from shapely.geometry import LineString

# Set a random seed for reproducibility
# Setting this seed means the tree will have the same structure each time this code is run
random.seed(0)

# Define the starting parameters for the fractal tree
start_x, start_y = 0, 0       # Starting coordinates (origin point)
initial_angle = 90            # Starting angle in degrees; 90 points the initial branch upward
length = 10                   # Initial length of the first branch segment
recursion_depth = 7           # Maximum recursion depth, controlling the "height" and complexity of the tree
max_branches = 4              # Maximum number of branches per node (can vary per depth)

# Recursive function to draw fractal branches; uses Shapely for line geometry
def draw_branch(x, y, direction, length, depth):
    # Base case for recursion: if depth reaches zero, stop drawing branches
    if depth == 0:
        return

    # Calculate the end point of the current branch segment using trigonometry
    # np.cos and np.sin calculate horizontal and vertical components
    end_x = x + length * np.cos(direction)
    end_y = y + length * np.sin(direction)

    # Define a line segment from (x, y) to (end_x, end_y) using Shapely's LineString
    line = LineString([(x, y), (end_x, end_y)])

    # Plot the current branch
    plt.plot(*line.xy, color='black')  # Unpack x and y coordinates of the line

    # Randomly adjust angle change and length scaling for a more organic appearance
    angle_change = random.uniform(20, 40)  # Random angle change between branches in degrees
    length_scaling_factor = random.uniform(0.6, 0.8)  # Random factor to reduce branch length with each recursion

    # Calculate the length of new branches at this recursion level
    new_length = length * length_scaling_factor

    # Determine a random number of branches to split from the current branch
    num_branches = random.randint(1, max_branches)

    # Calculate the total angle spread across multiple branches to distribute them evenly
    total_angle = (num_branches - 1) * angle_change  # Total spread of the angles across branches
    starting_angle = -total_angle / 2  # Center branches by starting from negative and spreading to positive

    # Recursively draw each branch with modified direction and reduced length
    for i in range(num_branches):
        branch_angle = starting_angle + i * angle_change
        # Convert branch angle to radians and recursively call draw_branch for each new segment
        draw_branch(end_x, end_y, direction + np.radians(branch_angle), new_length, depth - 1)

# Set up the plot for visualizing the fractal tree pattern
plt.figure(figsize=(8, 8))  # Define the size of the figure (canvas)
plt.axis('equal')  # Set equal scaling for x and y axes to maintain aspect ratio of branches
plt.axis('off')  # Hide plot axes for a cleaner look

# Start drawing the fractal tree from the starting point and initial angle
draw_branch(start_x, start_y, np.radians(initial_angle), length, recursion_depth)

# Display the final fractal pattern
plt.show()  