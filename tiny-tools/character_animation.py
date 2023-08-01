import matplotlib.pyplot as plt
import numpy as np
from svg.path import parse_path, Line, CubicBezier, QuadraticBezier

character_strokes = [
    "M 132 240 Q 132 80 336 80",    # Stroke 1: Left vertical curve
    "M 336 80 C 540 80 540 240 336 240",    # Stroke 2: Top horizontal curve
    "M 336 240 L 336 400",    # Stroke 3: Vertical line
]

# Define animation parameters
duration = 1  # Animation duration in seconds

# Function to extract the vertices from different path commands
def get_vertices_from_path(path):
    vertices = []
    for segment in path:
        if isinstance(segment, Line):
            vertices.append([segment.start.real, segment.start.imag])
            vertices.append([segment.end.real, segment.end.imag])
        elif isinstance(segment, QuadraticBezier):
            vertices.append([segment.start.real, segment.start.imag])
            vertices.append([segment.control.real, segment.control.imag])
            vertices.append([segment.end.real, segment.end.imag])
        elif isinstance(segment, CubicBezier):
            vertices.append([segment.start.real, segment.start.imag])
            vertices.append([segment.control1.real, segment.control1.imag])
            vertices.append([segment.control2.real, segment.control2.imag])
            vertices.append([segment.end.real, segment.end.imag])
    return np.array(vertices)

# Function to animate the strokes one after another
def animate_strokes():
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set_axis_off()

    for i, stroke in enumerate(character_strokes):
        path_data = parse_path(stroke)
        path_vertices = get_vertices_from_path(path_data)
        path = plt.Polygon(path_vertices, closed=False, edgecolor="black", linewidth=5, fill=False)
        ax.add_patch(path)

        ax.set_xlim(100, 540)
        ax.set_ylim(80, 400)

        plt.draw()
        plt.pause(duration)

# Start the animation
animate_strokes()
