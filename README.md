# chaos_game_fractal_explorer

An implementation of the chaos game using the python turtle
package in a tkinter GUI.

Users are able to select how many sides the base shape has
as well as vertex restrictions to produce a hundreds of
fractals.

Vertex restrictions simply mean how many points forward 
we can jump between points. For example, if we have a four
sided shape with a restriction of [1, 2, 4] and we are
currently on the second point. This means the next selected
vertex could be 3, 4 or 2 again. 

![Chaos Game] (https://github.com/rhodriguerrier/chaos_game_fractal_explorer/blob/main/chaos_game_gui_example.png?raw=true)