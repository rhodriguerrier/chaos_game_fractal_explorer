import tkinter as tk
import turtle
from polygon_coordinates import PolygonCoordinates
import random
from itertools import chain, combinations


class ProductionPane(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set up initial window
        self.geometry("900x900")
        self.configure(bg="red")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Function to update which restrictions are available based on number of sides picked
        def update_restrictions_choices(*args):
            choices = []
            sides = [x for x in range(1, (sides_choice.get()+1))]
            subsets = list(chain.from_iterable(combinations(sides, r) for r in range(1, len(sides)+1)))

            for i in range(len(subsets)):
                choices.append(str(subsets[i]))
            print(choices)

            restrictions_choice.set(choices[0])
            menu = available_restrictions['menu']
            menu.delete(0, 'end')
            for restriction in choices:
                menu.add_command(label=restriction, command=lambda nums=restriction: restrictions_choice.set(nums))

        # Function to load points of selected shape
        def load_shape(num_sides, jump_options):
            trtl.clear()
            poly = PolygonCoordinates(0, 0, 240, 0, num_sides)
            vertex_coords = poly.get_polygon_coordinates()
            for coordinate in vertex_coords:
                trtl.goto(coordinate[0], coordinate[1])
                trtl.dot(10)

            current_x = random.randint(-240, 240)
            current_y = random.randint(-240, 240)
            rnd_vertex = random.randint(0, num_sides-1)
            for i in range(50000):
                next_x = current_x + ((vertex_coords[rnd_vertex][0] - current_x) * (1 / 2))
                next_y = current_y + ((vertex_coords[rnd_vertex][1] - current_y) * (1 / 2))
                trtl.goto(next_x, next_y)
                trtl.dot(1)
                current_x = next_x
                current_y = next_y
                rnd_vertex = self.circular_num_set(num_sides-1, rnd_vertex, jump_options)

            screen.update()

        # Create frame to organise widgets and graphics canvas
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, sticky="")

        title_label = tk.Label(main_frame, text="Chaos Game Fractal Explorer", font=("Helvetica", 26))
        title_label.grid(row=0, columnspan=2)

        canvas = tk.Canvas(main_frame, width=500, height=500)
        canvas.grid(row=1, column=0)

        sides_choice = tk.IntVar(self)
        # sides_choice.set(3)
        num_sides_choice = tk.OptionMenu(main_frame, sides_choice, 3, 4, 5, 6, 7, 8, 9, 10)
        num_sides_choice.grid(row=1, column=1)

        restrictions_choice = tk.StringVar()
        available_restrictions = tk.OptionMenu(main_frame, restrictions_choice, '')
        available_restrictions.grid(row=2, column=1)

        load_button = tk.Button(main_frame, text="Load Fractal",
                                command=lambda: load_shape(sides_choice.get(),
                                                           self.cnvt_to_proper_input(restrictions_choice.get())))
        load_button.grid(row=3, column=1)

        # Set up turtle for function draw fractal on later
        screen = turtle.TurtleScreen(canvas)
        trtl = turtle.RawTurtle(screen, visible=False)
        trtl.speed(0)
        trtl.up()
        screen.delay(0)
        screen.tracer(0, 0)
        sides_choice.trace('w', update_restrictions_choices)

    def circular_num_set(self, max_num, current_vertex, jump_options):
        jmp_vertices = random.choice(jump_options)
        sum_num = current_vertex + jmp_vertices
        if sum_num > max_num:
            sum_num -= (max_num + 1)
        return sum_num

    # Function to convert the string choice of restriction to list of actual integers
    def cnvt_to_proper_input(self, vertices_string):
        vertex_list = []
        for i in vertices_string:
            try:
                vertex_list.append(int(i))
            except:
                pass
        return vertex_list


app = ProductionPane()
app.mainloop()
