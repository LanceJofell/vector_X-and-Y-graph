import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
from matplotlib.widgets import Button
import numpy as np

#shapes with specified radii
def vector_triangle():
    return [[0, 1, 0.5, 0], [0, 0, 1, 0]]

def vector_square(side_length):
    x = [-side_length / 2, side_length / 2, side_length / 2, -side_length / 2, -side_length / 2]
    y = [-side_length / 2, -side_length / 2, side_length / 2, side_length / 2, -side_length / 2]
    return x, y

def vector_star():
    return [[0.5, 0.61, 0.81, 0.67, 0.75, 0.5, 0.25, 0.33, 0.19, 0.39], [0.9, 0.6, 0.6, 0.4, 0.1, 0.3, 0.1, 0.4, 0.6, 0.6]]

#Circle with specified radius
def vector_circle(radius):
    return plt.Circle((0.5, 0.5), radius, color='red', fill=True)

# Oval with specified radii (horizontal and vertical)
def vector_oval(horizontal_radius, vertical_radius):
    return Ellipse((0.5, 0.5), width=2 * horizontal_radius, height=2 * vertical_radius, angle=45, color='blue', fill=True)

# Rectangle with specified dimensions
def vector_rectangle(rectangle_width, rectangle_height):
    return Rectangle((0.1, 0.1), rectangle_width, rectangle_height, color='brown', fill=True)

# Functions to plot each shape
def plot_triangle(event):
    triangle_x, triangle_y = vector_triangle()
    plt.figure()
    plt.plot(triangle_x, triangle_y, label='Triangle')
    plt.fill(triangle_x, triangle_y, 'skyblue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Triangle')
    plt.grid()
    plt.axis('equal')
    plt.show()

def plot_square(event):
    side_length = 0.8
    square_x, square_y = vector_square(side_length)
    plt.figure()
    plt.plot(square_x, square_y, label='Square', color='green')
    plt.fill(square_x, square_y, 'green', alpha=0.3)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Square')
    plt.grid()
    plt.axis('equal')
    plt.show()

def plot_star(event):
    star_x, star_y = vector_star()
    plt.figure()
    plt.plot(star_x, star_y, label='Star')
    plt.fill(star_x, star_y, 'orange')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Star')
    plt.grid()
    plt.axis('equal')
    plt.show()

def plot_circle(event):
    radius = 0.5
    circle = vector_circle(radius)
    plt.figure()
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Circle')
    plt.grid()
    plt.gca().add_patch(circle)
    plt.axis('equal')
    plt.show()

def plot_oval(event):
    horizontal_radius = 0.6
    vertical_radius = 0.4
    oval = vector_oval(horizontal_radius, vertical_radius)
    plt.figure()
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Oval')
    plt.grid()
    plt.gca().add_patch(oval)
    plt.axis('equal')
    plt.show()

def plot_rectangle(event):
    rectangle_width = 0.8
    rectangle_height = 0.6
    rectangle = vector_rectangle(rectangle_width, rectangle_height)
    plt.figure()
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Rectangle')
    plt.grid()
    plt.gca().add_patch(rectangle)
    plt.axis('equal')
    plt.show()

# Create buttons for each shape
fig, ax = plt.subplots(figsize=(10, 6))

# button properties
button_triangle = Button(plt.axes([0.1, 0.85, 0.1, 0.05]), 'Triangle')
button_square = Button(plt.axes([0.25, 0.85, 0.1, 0.05]), 'Square')
button_star = Button(plt.axes([0.4, 0.85, 0.1, 0.05]), 'Star')
button_circle = Button(plt.axes([0.55, 0.85, 0.1, 0.05]), 'Circle')
button_oval = Button(plt.axes([0.7, 0.85, 0.1, 0.05]), 'Oval')
button_rectangle = Button(plt.axes([0.85, 0.85, 0.1, 0.05]), 'Rectangle')

# click  functions 
button_triangle.on_clicked(plot_triangle)
button_square.on_clicked(plot_square)
button_star.on_clicked(plot_star)
button_circle.on_clicked(plot_circle)
button_oval.on_clicked(plot_oval)
button_rectangle.on_clicked(plot_rectangle)

plt.show()
