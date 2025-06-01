# this is my individual coding project python file

from tkinter import * # imports all modules from tkinter
from tkinter import ttk # imports themed tkinter from tkinter
from turtle import * # imports all modules from tutrle
import importlib
import random # imports random for use in randomly generating numbers
import math

#importlib.reload(*) # forces turtle to be reloaded to prevent crashing



def home_window(): # function responsible for the master/home page

    master = Tk() # create a master window
    master.title("Particle Simulator - Home Page") # name the window

    screen_w = master.winfo_screenwidth() # finds out the current screen's width
    screen_h = master.winfo_screenheight() # finds out the current screen's height
    center_x = screen_w//6 # floors the screen width by 6 to find the central x coord
    center_y = screen_h//6 # floors the screen height by 6 to find the central y coord

    master.geometry(f"800x500+{center_x}+{center_y}") # set the window dimensions

    home_title = Label(master, text="PARTICLE SIMULATOR", font=("Impact", 30)) # creates a title
    home_title.place(x=250, y=100) # places the title at the top middle of the window

    exit_button = Button(master, text="Exit", font=(15), padx=70, command=master.destroy, # creates an exit button, when clicked it destroys the master window, hence quitting the program
                          cursor="hand2", activebackground="lightgrey", activeforeground="black", background="lightpink")
    exit_button.place(x=315, y=250) # places the exit button in the middle of the screen, between the enter and options buttons

    options_button = Button(master, text="Options", font=(15), padx=52, # creates an options button
                          cursor="hand2", activebackground="lightgrey", activeforeground="black", background="lightblue")
    options_button.place(x=315, y=300) # places the options button in the middle of the screen, below the exit button


    
    def simulator_window(): # function responsible for the simulator page



        neon_vdw_attraction = 0.208 # van der Waals attraction factor (a) for Neon in barL^2/mol^2
        neon_collision_rad = 3 # approximate atomic interaction range
        

        # CREATING THE SIMULATOR WINDOW
        simulator_win = Toplevel(master) # creates a window on top of the home page window for the simulator
        simulator_win.title("Particle Simulator - Simulator Page") # gives the simulator window a window title
        simulator_win.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and places it in the middle of the screen

        # CREATING A TITLE ON SIMULATOR WINDOW
        part_num_title = Label(simulator_win, text="Number of particles:")
        part_num_title.place(x=20, y=125)

        numofparts = StringVar() # defines a String Variable
        typeofpart = StringVar()

        # CREATING AN ENTRY BOX ON SIMULATOR WINDOW
        part_num_entry = Entry(simulator_win, textvariable=numofparts, cursor="hand2") # creates an entry box for the number of particles to be added
        part_num_entry.place(x=20,y=150)

        part_types_list = ["Helium", "Neon", "Argon"]
        part_type_dropdown = ttk.Combobox(simulator_win, textvariable=typeofpart, cursor="hand2", values=part_types_list)
        part_type_dropdown.set("Choose a particle type")
        part_type_dropdown.place(x=20, y=50)



        # CREATING A TKINTER CANVAS ON SIMULATOR_WINDOW
        simulator_can = Canvas(simulator_win, height=300, width=300) # creates a white canvas in the middle of the window
        simulator_can.place(x=250, y=75) # places the canvas in the middle of the screen

        # CREATING A TURTLE CANVAS ON THE TKINTER CANVAS ON SIMULATOR WINDOW
        turt_can = TurtleScreen(simulator_can) # makes the canvas a turtle canvas
        turt_can.bgcolor("black") # makes the canvas black

        turt_can.listen() # makes the turtle canvas listen out for any events that may occur
        turt_can.tracer(0) # hides any turtle animation, including the black arrow

        # CREATING A BOUNDARY BOX IN THE TURTLE CANVAS
        box = RawTurtle(turt_can) # creates the turtle responsible for the boundary box of the particles
        box.hideturtle() # hides the turtle shape
        box.color("darkgrey") # makes the colour of the turtle dark grey
        box.pensize(10) # makes the turtle pen size 10
        box.shape("square") # changes the turtle shape to a square
        box.penup() # lifts the turtle pen up off the window so no traces are left
        box.speed(0) # sets the turtle speed to 0 - this special setting means the turtle animation occurs almost instantly/as fast as possible
        box.goto(-145,-145) # places the turtle at the bottom left of the black turtle canvas
        box.setheading(90) # makes the turtle face north
        box.pendown() # puts the turtle pen down, allowing any traces to be seen

        # DRAWS A BOUNDARY BOX IN THE BLACK TURTLE CANVAS
        for i in range(2): # loops twice, each time draws 2 sides
            box.forward(290) # moves the turtle forward by 290
            box.right(90) # turns the turtle to the right by 90 degrees
            box.forward(290) # moves the turtle forward by 290
            box.right(90) # turns the turtle to the right by 90 degrees
        box.penup() # lifts the pen up as no more drawings are needed

        
        
                
    
    
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
        
        temp = 0

        def get_temp(temp_from_scale):
            global temp
            temp = temp_scale.get()
            print(temp_from_scale)

        # CREATING A TEMPERATURE SCALE
        temp_scale = Scale(simulator_win, label="Temperature scale", from_=500, to=0, length=200, cursor="hand2", command=get_temp) # creates a temperature scale for changing the temperature
        temp_scale.place(x=600,y=100)


            

        def get_parts(): # function responsible for dealing with the number of particles inputted
            
            int_numofparts = int(numofparts.get()) # makes numofparts an integer
            if numofparts.get() == "":
                print("Number of particles: 0")
            else:
                print("Number of particles:", numofparts.get())

            class Particle(RawTurtle): # class responsible for controlling each particle
            #part = RawTurtle(turt_can)

                def __init__(self, turt_can, colour, speed, temp, rad=neon_collision_rad): # method responsible for initialising the particle's attributes e.g. color
        
                    super().__init__(turt_can)
                    #self = RawTurtle(turt_can)
                    print("innit works")
                    print("temperature=", temp)
                    self.hideturtle() # hides the current turtle
                    self.speed(0) # sets the turtle speed to 0 - this special setting means the turtle animation occurs almost instantly/as fast as possible
                    self.penup() # lifts the pen up
                    self.shape("circle") # changes the turtle shape to a circle
                    self.turtlesize(stretch_wid=1, stretch_len=1) # changes the size of the turtle shape
                    self.pencolor(colour) # makes the outline of the turtle blue
                    self.fillcolor(colour) # makes the fill of the turtle blue
                    self.pensize(5) # makes the turtle pen size 5
                    self.goto(random.randint(-130, 129),random.randint(-129, 130)) # places the current turtle at a random position within the turtle canvas
                    self.dx = speed * (temp * temp_factor) # sets the change in x of the turtle to speeed
                    self.dy = speed * (temp * temp_factor) # sets the change in y of the turtle to speed
                    self.radius = rad
                    self.temp_from_scale = temp
                    self.showturtle() # shows the current turtle
                    turt_can.update() # updates the turtle canvas
                    #turt_can.tracer(1)
                    #print(vars(self))

                    #self.move_particle()

                def move_particle(self, particles_list): # method responsible for the movement of the particles
                    #print("move_particle is running")

                    # MOVES THE PARTICLE
                    new_xcor = self.xcor() + self.dx # moves the particle by dx
                    new_ycor = self.ycor() + self.dy # moves the particle by 

                    # BOUNCES THE PARTICLE OFF THE BOUNDARY BOX
                    if new_xcor < -130 or new_xcor > 129: # if the x coordinates of the particle exceeds the boundary box
                        #self.setx(100)
                        self.dx *= -1 # inverts the dx, hence bouncing the particle off the boundary box
                    if new_ycor < -129 or new_ycor > 130: # if the y coordinates of the particle exceeds the boundary box
                        #self.sety(100)
                        self.dy *= -1 # inverts the dy, hence bouncing the particle off the boundary box
                    
                    # ATTRACTION AND REPULSION BETWEEN PARTICLES
                    for part in particles_list:
                        
                        if part != self:
                            
                            changeinx = part.xcor() - self.xcor()
                            changeiny = part.ycor() - self.ycor()
                            distance = math.sqrt(changeinx**2 + changeiny**2)

                            if neon_collision_rad < distance < 100:
                                
                                force = -neon_vdw_attraction / (distance**2)
                                self.dx += force * changeinx
                                self.dx += force * changeiny
                    
                    
                    self.goto(new_xcor, new_ycor)

            particles_list = [] # creates an empty list to be used for storing all of the particle turtles
            for i in range(int_numofparts): # loops for the number of particles added by the user
                colour = "pink" # defines colour as blue
                speed = 100 # defines speed as 2
                temp_factor = 0.01 # defines temp_factor as 0.01
                particle = Particle(turt_can, colour, speed, temp, neon_collision_rad) # calls the particle class, passing turt_can, colour and speed as parameters
                particles_list.append(particle) # adds the current particle turtle to the list of particles

            def keep_parts_moving(): # function responsible for the infinite movement of the particles
    
                for particle in particles_list: # loops through all of the particles in the list
                    particle.move_particle(particles_list) # calls the move_particle method
                turt_can.update() # updates the turtle canvas
                turt_can.ontimer(keep_parts_moving, 50)

            keep_parts_moving() # calls the keep_parts_moving function


        part_type_button = Button(simulator_win, text="Submit", cursor="hand2")
        part_type_button.place(x=175, y=48)

        part_num_button = Button(simulator_win, text="Submit", cursor="hand2", command=get_parts) # creates a submit button, when clicked calls the get_submit function
        part_num_button.place(x=150, y=150)
                


    #turt_can.update() # updates the canvas so we can now see turtle animations but the black arrow is hidden

    def options_window(): # function responsible for the options window
        pass

    enter_button = Button(master, text="Enter the simulator", font=(15), command=simulator_window,
                          cursor = "hand2", activebackground="lightgrey", activeforeground="black", background="lightgreen")
    enter_button.place(x=315, y=200)

    master.mainloop()


home_window()

    

