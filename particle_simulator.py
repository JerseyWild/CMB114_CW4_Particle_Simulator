# this is my individual coding project python file

from tkinter import * # imports all modules from tkinter
from tkinter import ttk # imports themed tkinter from tkinter
import turtle as turt
import importlib

importlib.reload(turt) # forces turtle to be reloaded to prevent crashing


def simulator_window(): # function responsible for the simulator page
    simulator_win = Toplevel(master) # creates a window on top of the home page window for the simulator
    simulator_win.title("Particle Simulator - Simulator Page") # gives the simulator window a window title
    simulator_win.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and places it in the middle of the screen
    simulator_can = Canvas(simulator_win, height=300, width=300) # creates a white canvas in the middle of the window

    turt_can = turt.TurtleScreen(simulator_can) # makes the canvas a turtle canvas
    turt_can.bgcolor("white") # makes the canvas black
    turt_can.tracer(n=None, delay=None)
    simulator_can.place(x=250, y=75) # places the canvas in the middle of the screen
    turt_can.update()
    numofparts = StringVar() # defines a String Variable
    def add_particles(): # function responsible for
        turt_can.update()
        int_numofparts = int(numofparts.get())
        if numofparts.get() == "":
            print("Number of particles: 0")
        else:
            print("Number of particles:", numofparts.get())
        turts_list = []
        for i in range(int_numofparts):
            turt_can.tracer(n=None, delay=None)
            #turts_list.append(turt.RawTurtle(turt_can))
        turt_can.update()
##        for i in range (len(turts_list)):
##            turts_list[i].hideturtle()
##            turts_list[i].penup()
##
##            turts_list[i].shape("circle")
##            turts_list[i].turtlesize(stretch_wid=1, stretch_len=1)
##            turts_list[i].pencolor("blue")
##            turts_list[i].fillcolor("blue")
##            turts_list[i].pensize(5)
##            
##            turts_list[i].goto(-140,-139)
##            turts_list[i].showturtle()
##            turts_list[i].goto(0,0)

    part_num_title = Label(simulator_win, text="Number of particles:")
    part_num_title.place(x=50, y=25)
    
    part_num_entry = Entry(simulator_win, textvariable=numofparts)
    part_num_entry.place(x=50,y=50)
    
    part_num_button = Button(simulator_win, text="Submit", command=add_particles)
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
