# Assignment 2: Fractal Generation Documentation

## Table of Contents

- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Results](#results)
- [Challenges and Solutions](#challenges-and-solutions)
- [References](#references)

---

## Pseudo-Code

*(Provide detailed pseudo-code explaining the logic of your program. This should clearly outline your recursive functions, parameter definitions, and how they contribute to the final fractal pattern.)*

Example:

1. **Define Main Function `generate_fractal(start_point, angle, length, depth)`**
   - **Inputs**:
     - `start_point`: Tuple of coordinates (x, y).
     - `angle`: Current angle in degrees.
     - `length`: Length of the current line segment.
     - `depth`: Current recursion depth.
   - **Process**:
     - **If** `depth` is 0:
       - **Return** (End recursion).
     - **Else**:
       - Calculate `end_point` using trigonometry:
         - `end_x = start_x + length * cos(radians(angle))`
         - `end_y = start_y + length * sin(radians(angle))`
       - Create a line from `start_point` to `end_point` using Shapely.
       - **For** each branch (e.g., left and right):
         - **Calculate** new angle:
           - Left branch: `new_angle = angle + angle_change`
           - Right branch: `new_angle = angle - angle_change`
         - **Calculate** new length:
           - `new_length = length * length_scaling_factor`
         - **Recursive Call**:
           - `generate_fractal(end_point, new_angle, new_length, depth - 1)`
     - **Return** (After recursive calls).

2. **Initialize Parameters**
   - Set `start_point`, `initial_angle`, `initial_length`, `recursion_depth`, `angle_change`, `length_scaling_factor`.

3. **Call `generate_fractal` Function**
   - Begin the fractal generation by calling `generate_fractal(start_point, initial_angle, initial_length, recursion_depth)`.

4. **Visualization**
   - Collect all the lines generated.
   - Use Matplotlib to plot the lines.
   - Apply any visualization enhancements (colors, line widths).

---

## Technical Explanation

In this approach, the `draw_branch` function uses recursion to generate a fractal tree pattern, where each branch splits into a random number of smaller branches, creating a tree-like structure. This recursive approach is based on trigonometry and randomness to calculate the position, direction, and branching of each line segment.

Starting from an initial point, angle, and length, `draw_branch` calculates the endpoint of each branch using trigonometric functions. At each recursive step, the function:

- Reduces the Branch Length: The length of each new branch is scaled down by a randomly chosen `length_scaling_factor`.
- Adjusts the Angle: A random `angle_change` between 20 and 40 degrees is applied to each branch, allowing for organic variations in direction. 
- Randomizes the Number of Branches: The number of branches emerging from each node is determined randomly, up to a maximum `max_branches`. This randomness adds further natural variation.
- Draws and Colors Each Branch: The Shapely library is used to define each branch geometrically, and matplotlib plots it with a color based on depth.

The recursion ends when the depth reaches zero, producing a finite fractal. By applying randomness to the number of branches, length, and angle at each level, a natural and complex pattern is achieved.

---

## Results

*(Include images of your generated fractal patterns, and discuss any observations or interesting findings.)*

Example:

### Fractal Pattern 1: Basic Fractal Tree

![Fractal Tree](images/example.png)

- **Parameters**:
  - `angle_change`: 30°
  - `length_scaling_factor`: 0.7
  - `recursion_depth`: 5
- **Observations**:
  - The fractal tree exhibits symmetry and balance.
  - As the recursion depth increases, the level of detail in the branches increases.

*(Repeat for other fractal patterns.)*

---

## Challenges and Solutions

*(Discuss any challenges you faced during the assignment and how you overcame them.)*

Example:

- **Challenge**: Managing the growing number of line segments and ensuring they are correctly plotted.
  - **Solution**: Stored all line segments in a list and plotted them after the recursion completed.

- **Challenge**: Implementing randomness without losing the overall structure.
  - **Solution**: Introduced randomness within controlled bounds for angles and lengths.

---

## References

*(List any resources you used or found helpful during the assignment.)*

- **Shapely Manual**: [https://shapely.readthedocs.io/en/stable/manual.html](https://shapely.readthedocs.io/en/stable/manual.html)
- **Matplotlib Pyplot Tutorial**: [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

---

*(Feel free to expand upon these sections to fully capture your work and learning process.)*