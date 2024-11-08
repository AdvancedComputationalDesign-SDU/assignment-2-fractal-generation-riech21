"""
Assignment 2: Fractal Generator

Author: Rie Pilgaard Christiansen

Description:
This script generates fractal patterns using recursive functions and geometric transformations.
"""

# Importing libraries for plotting and geometry manipulation
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

# Define the initial parameters for the fractal tree structure
start_x, start_y = 0, 0       # Starting coordinates at the origin (base of the tree)
initial_angle = 90            # Starting angle in degrees; 90 points the initial branch upward
length = 10                   # Initial length of the first branch segment
recursion_depth = 7           # Maximum recursion depth, controlling the "height" and complexity of the tree
angle_change = 30             # Fixed angle for each branch, creating a symmetrical spread
length_scaling_factor = 0.7   # Fixed factor to reduce branch length at each recursion level

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
 
    # Calculate the length of new branches at this recursion level
    new_length = length * length_scaling_factor

    # Recursively draw two branches from the current endpoint with modified direction and reduced length
    # Draw left branch with a negative angle change
    draw_branch(end_x, end_y, direction + np.radians(-angle_change), new_length, depth - 1)
    # Draw right branch with a positive angle change
    draw_branch(end_x, end_y, direction + np.radians(angle_change), new_length, depth - 1)

# Set up the plot for visualizing the fractal tree pattern
plt.figure(figsize=(8, 8))  # Define the size of the figure (canvas)
plt.axis('equal')  # Set equal scaling for x and y axes to maintain aspect ratio of branches
plt.axis('off')  # Hide plot axes for a cleaner look

# Start drawing the fractal tree from the starting point and initial angle
draw_branch(start_x, start_y, np.radians(initial_angle), length, recursion_depth)

# Display the final fractal pattern
plt.show() 