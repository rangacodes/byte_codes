import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from matplotlib.collections import PolyCollection

# Parameters
radius = 1.5  # Radius of the circle that the center traces
line_length = 6  # Length of the line
num_frames = 500  # Number of frames in the animation
rotation_speed = 3 * 2 * np.pi / num_frames  # Speed of center rotation

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Kakeya\'s solution to the needle problem')

# Create the line artist
line, = ax.plot([], [], 'r-', lw=2)

# Create a circle patch to show the path of the center
circle = patches.Circle((0, 0), radius, fill=False, color='orange', linestyle='--')
ax.add_patch(circle)


# Create points to show the center of the line
center_point, = ax.plot([], [], 'ro', markersize=6)
endpoint1, = ax.plot([], [], 'ro', markersize=6)
endpoint2, = ax.plot([], [], 'ro', markersize=6)

# Store the positions of the line at each frame
line_positions = []

# Create a polygon collection to represent the swept area
swept_area = PolyCollection([], alpha=0.2, facecolor='orange', edgecolor='none')
ax.add_collection(swept_area)

# Initialize function for the animation
def init():
    line.set_data([], [])
    center_point.set_data([], [])
    endpoint1.set_data([], [])
    endpoint2.set_data([], [])
    swept_area.set_verts([])
    return line, center_point, swept_area

# Update function for the animation
def update(frame):
    # Calculate the center position (tracing a circle)
    center_angle = frame * rotation_speed - np.pi / 2
    center_x = radius * np.cos(center_angle)
    center_y = radius * np.sin(center_angle)
    
    # Calculate the rotation angle of the line (half the speed)
    line_angle = - (center_angle + np.pi/2) / 2
    
    # Calculate the endpoints of the line
    dx = -(line_length / 2) * np.cos(line_angle)
    dy = -(line_length / 2) * np.sin(line_angle)
    
    x1 = center_x - dx
    y1 = center_y - dy
    x2 = center_x + dx
    y2 = center_y + dy
    
    # Update the line's data
    line.set_data([x1, x2], [y1, y2])
    
    # Update the center point
    center_point.set_data([center_x], [center_y])
    endpoint1.set_data([x1], [y1])
    endpoint2.set_data([x2], [y2])
    
    
    # Store the current line position
    line_positions.append([(x1, y1), (x2, y2)])
        
    # If we have enough positions, create polygons for the swept area
    if len(line_positions) > 1:
        polygons = []
        for i in range(len(line_positions) - 1):
            # Create a quadrilateral from two consecutive line positions
            quad = [
                line_positions[i][0],      # First point of current line
                line_positions[i][1],      # Second point of current line
                line_positions[i+1][1],    # Second point of next line
                line_positions[i+1][0]     # First point of next line
            ]
            polygons.append(quad)
        
        # Update the swept area
        swept_area.set_verts(polygons)
    
    return line, center_point, endpoint1, endpoint2, swept_area

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=50)

# Add a text explanation
text_str = """
The animation shows:

- Red dots: Center and endpoints of the line
- Red line: Rotating line
- Orange dashed circle: Path of the center
- Orange region: Area swept by the line

The line rotates around its center at half the angular speed 
of its center in the opposite direction
"""
ax.text(0.05, 0.05, text_str, transform=ax.transAxes, 
        bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
# plt.show()

# Uncomment the following line to save the animation as a GIF
ani.save('Kakeya\'s needle problem.gif', writer='pillow', fps=30)