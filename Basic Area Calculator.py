import math
import tkinter as tk
from tkinter import messagebox

def calculate_circle_area(radius):
    """Calculate the area of a circle given the radius."""
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle given the length and width."""
    return length * width

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle given the base and height."""
    return 0.5 * base * height

def calculate_square_area(side):
    """Calculate the area of a square given the side length."""
    return side ** 2

def save_to_file(shape, dimensions, area):
    """Save the calculated area to a file."""
    with open("area_calculations.txt", "a") as file:
        file.write(f"Shape: {shape}, Dimensions: {dimensions}, Area: {area:.2f} square meters\n")

def on_calculate():
    """Calculate the area based on user input and selected shape."""
    shape = shape_var.get()
    try:
        if shape == "Circle":
            radius = float(entry1.get())
            area = calculate_circle_area(radius)
            dimensions = f"radius = {radius} meters"
        elif shape == "Rectangle":
            length = float(entry1.get())
            width = float(entry2.get())
            area = calculate_rectangle_area(length, width)
            dimensions = f"length = {length} meters, width = {width} meters"
        elif shape == "Triangle":
            base = float(entry1.get())
            height = float(entry2.get())
            area = calculate_triangle_area(base, height)
            dimensions = f"base = {base} meters, height = {height} meters"
        elif shape == "Square":
            side = float(entry1.get())
            area = calculate_square_area(side)
            dimensions = f"side = {side} meters"
        result_var.set(f"The area of the {shape} is: {area:.2f} square meters")
        save_to_file(shape, dimensions, area)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def on_shape_change(*args):
    """Update input fields based on selected shape."""
    shape = shape_var.get()
    if shape in ["Circle", "Square"]:
        label2.grid_forget()
        entry2.grid_forget()
    else:
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)

root = tk.Tk()
root.title("Basic Area Calculator")

shape_var = tk.StringVar(value="Circle")
shape_var.trace("w", on_shape_change)

tk.Label(root, text="Shape:").grid(row=0, column=0)
shape_menu = tk.OptionMenu(root, shape_var, "Circle", "Rectangle", "Triangle", "Square")
shape_menu.grid(row=0, column=1)

tk.Label(root, text="Dimension 1 (meters):").grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

label2 = tk.Label(root, text="Dimension 2 (meters):")
entry2 = tk.Entry(root)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row=3, columnspan=2)

tk.Button(root, text="Calculate", command=on_calculate).grid(row=4, columnspan=2)

on_shape_change()  # Initialize the correct fields based on the default shape

root.mainloop()
