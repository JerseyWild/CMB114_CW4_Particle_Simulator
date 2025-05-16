# this is my individual coding project python file

from tkinter import * # imports all modules from tkinter
from tkinter import ttk # imports themed tkinter from tkinter
import turtle as turt
import importlib

importlib.reload(turt) # forces turtle to be reloaded to prevent crashing


def simulator_window(): # function responsible for the simulator page
    simulator_win = Toplevel(master)
    simulator_win.title("Particle Simulator - Simulator Page")
    simulator_win.geometry(f"800x500+{center_x}+{center_y}")
    simulator_can = Canvas(simulator_win, bg="black", height=300, width=300)

    turt_can = turt.TurtleScreen(simulator_can)
    #turt_can.tracer(0)
    turt_can.bgcolor("black")

    simulator_can.place(x=250, y=75)

    numofparts = StringVar()
    def submit_entry():
        if numofparts.get() == "":
            print("Number of particles: 0")
        else:
            print("Number of particles:", numofparts.get())
        
    part_num_entry = Entry(simulator_win, textvariable=numofparts)
    part_num_entry.place(x=50,y=50)
    part_num_button = Button(simulator_win, text="Submit", command=submit_entry)
    part_num_button.place(x=180, y=45)


def particles():
    turtle = turt.RawTurtle(turt_can)
    turtle.color("white")
    turtle.forward(40)
    

master = Tk() # create a master window
master.title("Particle Simulator - Home Page") # name the window

screen_w = master.winfo_screenwidth() # finds out the current screen's width
screen_h = master.winfo_screenheight() # finds out the current screen's height
center_x = screen_w//6 # floors the screen width by 6 to find the central x coord
center_y = screen_h//6 # floors the screen height by 6 to find the central y coord


master.geometry(f"800x500+{center_x}+{center_y}") # set the window dimensions

home_title = Label(master, text="PARTICLE SIMULATOR", font=("Impact", 30))
home_title.place(x=250, y=100)

enter_button = Button(master, text="Enter the simulator", font=(15), command=simulator_window,
                      activebackground="lightgrey", activeforeground="black", background="lightgreen")
enter_button.place(x=315, y=200)

exit_button = Button(master, text="Exit", font=(15), padx=70, command=master.destroy,
                      activebackground="lightgrey", activeforeground="black", background="lightpink")
exit_button.place(x=315, y=250)

options_button = Button(master, text="Options", font=(15), padx=52,
                      activebackground="lightgrey", activeforeground="black", background="lightblue")
options_button.place(x=315, y=300)




master.mainloop()
