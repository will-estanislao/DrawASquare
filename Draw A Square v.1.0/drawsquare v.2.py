#   Title:          Draw Your Own Squares
#   Author:         Willert
#   Date:           13/03/21
#   
#   Description:    A fun little program that will let you "draw" your own
#                   squares. No art skills? No problem! Just automate your art!
#                   The user can create a square with the press of a button. The
#                   initial position of the pen can also be moved around. The colours
#                   and pen size can be customized.

# Imports
import turtle
import tkinter as tk


# Declare variables and constants
SQUARE = 4
INITIAL_SIZE = 50
FORWARD_VALUE = 100
INITIAL_TURN = 90
TURN_VALUE = 22.5
pen_move = False

# To view how turtle functions are working
# testwindow = turtle.Screen()

# Create tk instance
window = tk.Tk()
# Set the properties of the window
window.geometry("600x350")
window.minsize(width = 600, height = 350)
window.title("Draw A Square")
window.configure(bg = "blue")
window.resizable(False, False)

# Frame for content
# Frame for main content widgets
content = tk.Frame(window, borderwidth = 2, bg = 'turquoise', relief = "raised", width = 100, height = 400)
content.grid(row = 0, column = 0, rowspan = 5, sticky = 'NS')


# Frame for canvas
canvas_frame = tk.Frame(borderwidth = 3, relief = "ridge", width = 450, height = 310)
canvas_frame.grid(row = 0, column = 1, columnspan = 5, rowspan = 5, sticky = 'NE', padx = 5, pady = 5)

# Canvas with window
canvas = tk.Canvas(canvas_frame)
canvas.config(width = 450, height = 330)
canvas.grid(row = 0, column = 1, columnspan = 5, sticky = 'NE')

# Turtle cursor pen
square_draw = turtle.RawTurtle(canvas)
square_draw.setheading(90)

# Tooltips window
# tooltips = Balloon(window)

# Functions for UI
# Drawing the square
def draw_square():
    for drawing in range(SQUARE):
        square_draw.pd()
        square_draw.forward (FORWARD_VALUE)
        square_draw.right (INITIAL_TURN)

# Changing the size
new_size = tk.IntVar()
def pensizeselect(self):
    user_penvalue = new_size.get()
    square_draw.width(user_penvalue)

# Change Colours
new_colour = tk.StringVar()
new_colour.set('black')
def colourselect():
    pen_colour = new_colour.get()
    square_draw.fillcolor(pen_colour)
    square_draw.pencolor(pen_colour)

# Clear screen
def clearscreen():
    square_draw.clear()
# Undo previous action
def undo_button():
    square_draw.undo()
# Reset cursor on canvas
def reset_canvas():
    square_draw.pu()
    square_draw.goto(0,0)
    square_draw.setheading(90)

# Move pen in different directions
# Move pen forwards in the current direction it is facing
def move_forward():
    square_draw.penup()
    square_draw.forward(50)   
    square_draw.pendown()

# Move pen backwards
def move_down():
    square_draw.penup()
    square_draw.backward(50)   
    square_draw.pendown()

# Turn pen towards the right
def turn_right():
    square_draw.right(TURN_VALUE)

# Turn pen towards the left
def turn_left():
    square_draw.left(TURN_VALUE)


# Button for creating a square
button_create_square = tk.Button(content, text = "DRAW SQUARE", width = 15, bg = 'gold', relief = "raised", command = draw_square)
button_create_square.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'S')
# tooltips.bind_widget(button_create_square, msg = "The draw a square button! It'll draw a square, try it out.")

# Button for undo, clear & reset
button_undo = tk.Button(content, text = "UNDO", width = 15, bg = 'gold', command = undo_button)
button_undo.grid(row = 1, column = 0, padx = 5)
button_clear = tk.Button(content, text = "CLEAR", width = 5, bg = 'gold', command = clearscreen)
button_clear.grid(row = 0, column = 0, padx = 15, pady = 2, sticky = 'W')
button_reset = tk.Button(content, text = "RESET", width = 5, bg = 'gold', command = reset_canvas)
button_reset.grid(row = 0, column = 0, padx = 15, sticky = 'E')
# tooltips for these button functions
# tooltips.bind_widget(button_undo, msg = "This will undo 1 action.")
# tooltips.bind_widget(button_clear, msg = "This will erase all squares on the canvas.")
# tooltips.bind_widget(button_reset, msg = "Resets the position of your pen back to it's original position.")

# Buttons for directions
# Up
button_up = tk.Button(content, text = "^", width = 5, bg = 'orchid', command = move_forward)
button_up.grid(row = 3, column = 0, padx = 5, sticky = 'S')
# Down
button_down = tk.Button(content, text = "v", width = 5, bg = 'orchid', command = move_down)
button_down.grid(row = 5, column = 0, padx = 5, sticky = 'S')
# Left
button_left = tk.Button(content, text = "<", width = 5, bg = 'orchid', command = turn_left)
button_left.grid(row = 4, column = 0, padx = 5, pady =5, sticky = 'SW')
# Right
button_right = tk.Button(content, text = ">", width = 5, bg = 'orchid', command = turn_right)
button_right.grid(row = 4, column = 0, padx = 5, pady =5, sticky = 'SE')

# Colour Pallete
label_colour = tk.Label(content, bg = "pink" , relief = "sunken", text = "COLOUR: ")
label_colour.grid(row = 6, column = 0, padx = 5, pady =5, sticky = 'SW')
# Colour Pallette choice
rb1_colour = tk.Radiobutton(content, bg = "black", fg = 'white', relief = "sunken", text = "BLACK", variable = new_colour, value = 'black', selectcolor = 'hotpink', 
command = colourselect, indicatoron = 0, width = 7)
rb2_colour = tk.Radiobutton(content, bg = "red", fg = 'white', relief = "sunken", text = "RED", variable = new_colour, value = 'red', selectcolor = 'hotpink',
command = colourselect, indicatoron = 0, width = 7)
rb3_colour = tk.Radiobutton(content, bg = "blue", fg = 'white', relief = "sunken", text = "BLUE", variable = new_colour, value = 'blue', selectcolor = 'hotpink',
command = colourselect, indicatoron = 0, width = 7)
rb4_colour = tk.Radiobutton(content, bg = "yellow", fg = 'black', relief = "sunken", text = "YELLOW", variable = new_colour, value = 'yellow', selectcolor = 'hotpink',
command = colourselect, indicatoron = 0, width = 7)
rb1_colour.grid (row = 7, column = 0, padx = 5, sticky = 'W')
rb2_colour.grid (row = 7, column = 0, padx = 5, columnspan = 3, sticky = 'E')
rb3_colour.grid (row = 8, column = 0, padx = 5, columnspan = 3, sticky = 'W')
rb4_colour.grid (row = 8, column = 0, padx = 5, columnspan = 3, sticky = 'E')
# tooltips.bind_widget(label_colour, msg = "Choose pen colours.")

# Size choice labels
label_size = tk.Label(content, bg = "pink", relief = "sunken", text = "Pen Size: ")
label_size.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = 'SW')
# tooltips.bind_widget(label_size, msg = "Adjust your pen size. Minimum is 1 and maximum is 50")
# Size choice
scale_size = tk.Scale(content, length = 110, width = 15, from_=1.0, to = 50.0, bg = 'skyblue', troughcolor = 'steelblue',
orient = tk.HORIZONTAL ,bd = 0 ,variable = new_size, command = pensizeselect)
scale_size.grid(row = 10, column = 0, padx = 2, sticky = 'S')


window.mainloop()