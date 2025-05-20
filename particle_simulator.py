# this is my individual coding project python file

from tkinter import * # imports all modules from tkinter
from tkinter import ttk # imports themed tkinter from tkinter
from turtle import *
import importlib
import random

#importlib.reload(*) # forces turtle to be reloaded to prevent crashing

def home_window():

    master = Tk() # create a master window
    master.title("Particle Simulator - Home Page") # name the window

    screen_w = master.winfo_screenwidth() # finds out the current screen's width
    screen_h = master.winfo_screenheight() # finds out the current screen's height
    center_x = screen_w//6 # floors the screen width by 6 to find the central x coord
    center_y = screen_h//6 # floors the screen height by 6 to find the central y coord

    master.geometry(f"800x500+{center_x}+{center_y}") # set the window dimensions

    home_title = Label(master, text="PARTICLE SIMULATOR", font=("Impact", 30))
    home_title.place(x=250, y=100)

    exit_button = Button(master, text="Exit", font=(15), padx=70, command=master.destroy,
                          cursor="hand2", activebackground="lightgrey", activeforeground="black", background="lightpink")
    exit_button.place(x=315, y=250)

    options_button = Button(master, text="Options", font=(15), padx=52,
                          cursor="hand2", activebackground="lightgrey", activeforeground="black", background="lightblue")
    options_button.place(x=315, y=300)


    
    def simulator_window(): # function responsible for the simulator page

        # CREATING THE SIMULATOR WINDOW
        simulator_win = Toplevel(master) # creates a window on top of the home page window for the simulator
        simulator_win.title("Particle Simulator - Simulator Page") # gives the simulator window a window title
        simulator_win.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and places it in the middle of the screen

        # CREATING A TITLE ON SIMULATOR WINDOW
        part_num_title = Label(simulator_win, text="Number of particles:")
        part_num_title.place(x=50, y=25)

        numofparts = StringVar() # defines a String Variable

        # CREATING AN ENTRY BOX ON SIMULATOR WINDOW
        part_num_entry = Entry(simulator_win, textvariable=numofparts, cursor="hand2")
        part_num_entry.place(x=50,y=50)

        # CREATING A TEMPERATURE SCALE
        temp_scale = Scale(simulator_win, label="Temperature scale", from_=500, to=0, length=200, cursor="hand2")
        temp_scale.place(x=600,y=100)

        # CREATING A TKINTER CANVAS ON SIMULATOR_WINDOW
        simulator_can = Canvas(simulator_win, height=300, width=300) # creates a white canvas in the middle of the window
        simulator_can.place(x=250, y=75) # places the canvas in the middle of the screen

        # CREATING A TURTLE CANVAS ON THE TKINTER CANVAS ON SIMULATOR WINDOW
        turt_can = TurtleScreen(simulator_can) # makes the canvas a turtle canvas
        turt_can.bgcolor("black") # makes the canvas black

        turt_can.listen()
        turt_can.tracer(0) # hides any turtle animation, including the black arrow

        # CREATING A BOUNDARY BOX IN THE TURTLE CANVAS
        box = RawTurtle(turt_can)
        box.hideturtle()
        box.color("darkgrey")
        box.pensize(10)
        box.shape("square")
        box.penup()
        box.speed(0)
        box.goto(-145,-145)
        box.setheading(90)
        box.pendown()
        
        for i in range(2): # loops twice, each time draws 2 sides
            box.forward(290)
            box.right(90)
            box.forward(290)
            box.right(90)
        box.penup()

        
        
                
    
    
        # part = Particle()
    ##
    ##    for i in range(int_numofparts):
    ##    turt_can.tracer(0)
    ##
    ##    part.showturtle()
    ##    turt_can.tracer(1)
    ##
    ##    while True:
    ##    #turt_can.update()

    # -----------------------------------------------------------

        def get_submit():
            
            int_numofparts = int(numofparts.get())
            if numofparts.get() == "":
                print("Number of particles: 0")
            else:
                print("Number of particles:", numofparts.get())

            class Particle(RawTurtle): # controls each particle
            #part = RawTurtle(turt_can)

                def __init__(self, turt_can, colour, speed): # initialises the particle's attributes e.g. color

                    super().__init__(turt_can)
                    #self = RawTurtle(turt_can)
                    
                    self.hideturtle() # hides the current turtle
                    self.speed(0)
                    self.penup()
                    self.shape("circle")
                    self.turtlesize(stretch_wid=1, stretch_len=1)
                    self.pencolor(colour)
                    self.fillcolor(colour)
                    self.pensize(5)
                    self.goto(random.randint(-130, 129),random.randint(-129, 130))
                    self.dx = speed
                    self.dy = speed
                    self.showturtle()
                    turt_can.update()
                    #turt_can.tracer(1)
                    #print(vars(self))

                    #self.move_particle()

                def move_particle(self):
                    #print("move_particle is running")
                    
                    self.setx(self.xcor() + self.dx)
                    self.sety(self.ycor() + self.dy)

                def bounce_particle(self):

                    if self.xcor() < -130 or self.xcor() > 129:
                        #self.setx(100)
                        self.dx *= -1
                    if self.ycor() < -129 or self.ycor() > 130:
                        #self.sety(100)
                        self.dy *= -1
                    

            particles_list = []
            for i in range(int_numofparts):
                colour = "blue"
                speed = 2
                particle = Particle(turt_can, colour, speed)
                particles_list.append(particle)

            def keep_parts_moving():
    
                for particle in particles_list:
                    particle.move_particle()
                    particle.bounce_particle()
                turt_can.update()
                turt_can.ontimer(keep_parts_moving, 50)

            keep_parts_moving()


        part_num_button = Button(simulator_win, text="Submit", cursor="hand2", command=get_submit)
        part_num_button.place(x=180, y=45)

    #turt_can.update() # updates the canvas so we can now see turtle animations but the black arrow is hidden

    def options_window():
        pass

    enter_button = Button(master, text="Enter the simulator", font=(15), command=simulator_window,
                          cursor = "hand2", activebackground="lightgrey", activeforeground="black", background="lightgreen")
    enter_button.place(x=315, y=200)

    master.mainloop()


home_window()

    

