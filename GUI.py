import tkinter as tk
from tkinter.ttk import *
import turtle
from polygon_coordinates import PolygonCoordinates
import random


class ProductionPane(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set up initial window
        self.geometry("900x900")
        self.configure(bg="red")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Function to load points of selected shape
        def load_shape(num_sides):
            trtl.clear()
            poly = PolygonCoordinates(0, 0, 240, 0, num_sides)
            vertex_coords = poly.get_polygon_coordinates()
            for coordinate in vertex_coords:
                trtl.goto(coordinate[0], coordinate[1])
                trtl.dot(10)
            screen.update()

        # Create frame to organise widgets and graphics canvas
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, sticky="")

        title_label = tk.Label(main_frame, text="Chaos Game Fractal Explorer", font=("Helvetica", 26))
        title_label.grid(row=0, columnspan=2)

        canvas = tk.Canvas(main_frame, width=500, height=500)
        canvas.grid(row=1, column=0)

        sides_choice = tk.IntVar(self)
        num_sides = tk.OptionMenu(main_frame, sides_choice, 4, 5, 6, 7, 8, 9, 10)
        num_sides.grid(row=1, column=1)

        load_button = tk.Button(main_frame, text="Load Fractal",
                                command=lambda: load_shape(sides_choice.get()))
        load_button.grid(row=2, column=1)

        # Set up turtle for function draw fractal on later
        screen = turtle.TurtleScreen(canvas)
        trtl = turtle.RawTurtle(screen, visible=False)
        trtl.speed(0)
        trtl.up()
        screen.delay(0)
        screen.tracer(0, 0)


app = ProductionPane()
app.mainloop()
