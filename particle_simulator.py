
# ---------------------------------------------------JERSEY WILDEN CMB114 CW4 PARTICLE SIMULATOR PROGRAM --------------------------------------------

# IMPORTING ALL NECESSARY MODULES
from tkinter import * # imports all modules from tkinter
from tkinter import ttk # imports themed tkinter from tkinter
from turtle import * # imports all modules from tutrle
import random # imports random for use in randomly generating numbers
import math # imports math for use in square roots
from scipy import constants # imports constants from scipy for use in the ideal gas constant (R)
import time # imports time for use in the time elapsed counter


numofcollisions = 0
particles_list = []
collided_pairs = set()
stop_timer = False

# FUNCTION RESPONSIBLE FOR THE MASTER/HOME PAGE
def home_window():

    master = Tk() # create a master window
    master.title("Particle Simulator - Home Page") # name the window

    screen_w = master.winfo_screenwidth() # finds out the current screen's width
    screen_h = master.winfo_screenheight() # finds out the current screen's height
    center_x = screen_w//6 # floors the screen width by 6 to find the central x coord
    center_y = screen_h//6 # floors the screen height by 6 to find the central y coord

    master.geometry(f"800x500+{center_x}+{center_y}") # set the window dimensions

    master.configure(bg="lightblue")

    home_title = Label(master, text="PARTICLE SIMULATOR", font=("Impact", 40), bg="lightblue", fg="white") # creates a title
    home_title.place(x=200, y=100) # places the title at the top middle of the window

    exit_button = Button(master, text="Exit", font=(15), fg="white", padx=70, command=master.destroy, # creates an exit button, when clicked it destroys the master window, hence quitting the program
                          cursor="hand2", activebackground="lightgrey", activeforeground="black", background="firebrick1")
    exit_button.place(x=315, y=250) # places the exit button in the middle of the screen, between the enter and options buttons

    # FUNCTION RESPONSIBLE FOR THE SIMULATOR PAGE
    def simulator_window():
        
        global numofparts,numofparts_label, actual_max_speed_label, collision_count_label, time_elapsed_label
        
        # CREATING THE SIMULATOR WINDOW
        simulator_win = Toplevel(master) # creates a window on top of the home page window for the simulator
        simulator_win.title("Particle Simulator - Simulator Page") # gives the simulator window a window title
        simulator_win.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and places it in the middle of the screen
        simulator_win.configure(bg="mediumaquamarine")
        
        # CREATING A TITLE ON SIMULATOR WINDOW
        part_num_title = Label(simulator_win, text="Number of particles", bg="aquamarine")
        part_num_title.place(x=20, y=125)

        # CREATING AN ENTRY BOX ON SIMULATOR WINDOW
        numofparts = StringVar() # defines a String Variable
        part_num_entry = Entry(simulator_win, textvariable=numofparts, cursor="hand2") # creates an entry box for the number of particles to be added
        part_num_entry.place(x=20,y=150)

        # CREATING A LABEL ON SIMULATOR WINDOW FOR PARTICLE TYPE
        part_type_label = Label(simulator_win, text="Choose a particle type", bg="aquamarine")
        part_type_label.place(x=20, y=25)

        # CREATING A DROPDOWN MENU ON SIMULATOR WINDOW FOR PARTICLE TYPE
        typeofpart = StringVar()
        part_type_dropdown = ttk.Combobox(simulator_win, textvariable=typeofpart, cursor="hand2")
        part_type_dropdown["values"] = ["Helium", "Neon", "Argon"]
        part_type_dropdown.place(x=20, y=50)

        numofparts_label = Label(simulator_win, text=("Number of particles = " + str(len(particles_list))), font=("Courier New", 12), bg="aquamarine")
        numofparts_label.place(x=20, y=200)
        
        actual_max_speed_label = Label(simulator_win, text="Max speed = 0.00 m/s", font=("Courier New", 12), bg="aquamarine")
        actual_max_speed_label.place(x=20, y=225)

        collision_count_label = Label(simulator_win, text="Number of collisions = 0", font=("Courier New", 12), bg="aquamarine")
        collision_count_label.place(x=20, y=250)

        time_elapsed_label = Label(simulator_win, text="Time elapsed = 0.00 s", font=("Courier New", 12), bg="aquamarine")
        time_elapsed_label.place(x=20, y=275)

        # CREATING A TKINTER CANVAS ON SIMULATOR_WINDOW
        simulator_can = Canvas(simulator_win, height=300, width=300) # creates a white canvas in the middle of the window
        simulator_can.place(x=300, y=75) # places the canvas in the middle of the screen

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

        
        # CREATING A TEMPERATURE SCALE
        temp_scale = Scale(simulator_win, label="Temperature Scale (K)", from_=500, to=1, length=200,
                           cursor="hand2", bg="aquamarine") # creates a temperature scale for changing the temperature
        temp_scale.place(x=620,y=100)

        # FUNCTION RESPONSIBLE FOR DEALING WITH ALL PARTICLES ADDED
        def get_parts():
            global stop_timer, int_numofparts
            stop_timer = False
            int_numofparts = int(numofparts.get()) # makes numofparts an integer

            # CLASS RESPONSIBLE FOR THE PARTICLES AND THEIR MOVEMENT
            class Particle(RawTurtle): # class responsible for controlling each particle

                # METHOD RESPONSIBLE FOR INITIALISING VARIABLES
                def __init__(self, turt_can, colour, speed, current_temp): # method responsible for initialising the particle's attributes e.g. color

                    super().__init__(turt_can)

                    self.hideturtle() # hides the current turtle
                    self.speed(0) # sets the turtle speed to 0 - this special setting means the turtle animation occurs almost instantly/as fast as possible
                    self.penup() # lifts the pen up
                    self.shape("circle") # changes the turtle shape to a circle
                    # SIZE OF THE CURRENT PARTICLE CHOSEN. HELIUM DIAMETER = 0.22 pm
                    turtle_rad = 0.11*3
                    self.turtlesize(stretch_wid=turtle_rad*2, stretch_len=turtle_rad*2) # changes the size of the turtle shape
                    self.pencolor(colour) # makes the outline of the turtle blue
                    self.fillcolor(colour) # makes the fill of the turtle blue
                    self.pensize(5) # makes the turtle pen size 5
                    self.goto(random.randint(-130, 129),random.randint(-129, 130)) # places the current turtle at a random position within the turtle canvas
                    self.dx = (((3*constants.R * current_temp)/0.004)**0.5) * 0.01 # sets the change in x of the turtle to speeed
                    self.dy = (((3*constants.R * current_temp)/0.004)**0.5) * 0.01 # sets the change in y of the turtle to speed
                    self.radius = turtle_rad
                    self.temp = current_temp
                    
                    self.showturtle() # shows the current turtle
                    turt_can.update() # updates the turtle canvas

                
                # METHOD RESPONSIBLE FOR THE PARTICLES' MOVEMENT
                def move_particle(self, particles_list, current_temp, temp_factor): # method responsible for the movement of the particles 
        
                    actual_max_speed = ((3*constants.R * current_temp)/0.004)**0.5 # uses the root mean square speed (vRMS) formula to find the maximum possible speed based on the current temperature and molar mass of the particle type
                    actual_max_speed_label.config(text=f"Max speed = {actual_max_speed:.2f} m/s")

                    turtle_max_speed = actual_max_speed * 0.002 # scales the speed to a sensible level

                    for i in range(3):
                    
                        if self.temp != 0: # increases the speed of the current particles in proportion to temperature
                            scale_factor = (current_temp / self.temp) * temp_factor
                            self.dx *= scale_factor
                            self.dy *= scale_factor

                            self.dx = max(-turtle_max_speed, min(turtle_max_speed, self.dx)) # sets max vals for dx
                            self.dy = max(-turtle_max_speed, min(turtle_max_speed, self.dy)) # sets max vals for dy

                        self.temp = current_temp
                        
                        # MOVES THE PARTICLE
                        new_xcor = self.xcor() + self.dx # moves the particle by dx
                        new_ycor = self.ycor() + self.dy # moves the particle by 

                        # BOUNCES THE PARTICLE OFF THE BOUNDARY BOX
                        if new_xcor < -127 or new_xcor > 127: # if the x coordinates of the particle exceeds the boundary box
                          
                            self.dx *= -1 # inverts the dx, hence bouncing the particle off the boundary box
                            self.dx += random.uniform(-0.05, 0.05)
                        if new_ycor < -126 or new_ycor > 126: # if the y coordinates of the particle exceeds the boundary box
                     
                            self.dy *= -1 # inverts the dy, hence bouncing the particle off the boundary box
                            self.dx += random.uniform(-0.05, 0.05)
                    

                        for part in particles_list: # loops through all current particles

                            x_distanceapart = part.xcor() - self.xcor() # x distance apart between 2 particles from their center
                            y_distanceapart = part.ycor() - self.ycor() # y distance apart between 2 particles from their center
                            overall_distanceapart = math.sqrt(x_distanceapart**2 + y_distanceapart**2) # direct distance apart between 2 particles using Pythagoras' theorem
                            
                            if part != self and overall_distanceapart < 23: # if the 2 particles being investigated for collisions are different particles and their distance apart is < 10 in both x and y directions (to only test those particles close enough to collide - speeds up program)
                                
                                if overall_distanceapart <= 5*(2*(self.radius + part.radius)): # if the distance between the 2 particles is the sum of their radii this means they are touching
                                    collision_id = tuple(sorted([id(self), id(part)])) # gives the current collision a unique id
                                    global collided_pairs
                                    
                                    if collision_id not in collided_pairs: # if this collision has only occurred once/not before
                                        
                                        collided_pairs.add(collision_id)
                                        global numofcollisions
                                        numofcollisions += 1 # 1 more collision has occurred
                                        self.dx, part.dx = part.dx, self.dx
                                        self.dy, part.dy = part.dy, self.dy
                                        collision_count_label.config(text=("Number of collisions = " + str(numofcollisions))) # updates the collision label with the new collision (+1 collision)
                                        
        
                        self.goto(new_xcor, new_ycor) # move the new particle to the new x and y cords

            # FUNCTION RESPONSIBLE FOR THE TIME ELAPSED OF THE PARTICLES
            def end_time_func(start_t, t_elapsed_label):
                
                global end_t, stop_timer
                if stop_timer == True:
                    return
                end_t = time.time() # ends the timer
                t_elapsed_label.config(text=f"Time elapsed = {end_t-start_t:.2f} s") # prints the elapsed time
                simulator_win.after(1000, lambda: end_time_func(start_t, t_elapsed_label)) # refreshes the elapsed time


            global particles_list
            
            for i in range(int_numofparts): # loops for the number of particles added by the user
                
                colour = "pink" # defines colour as blue
                particle = Particle(turt_can, colour, speed, temp_scale.get()) # calls the particle class, passing turt_can, colour and speed as parameters
                particles_list.append(particle) # adds the current particle turtle to the list of particles
 
                if len(particles_list) == 1 and i == 0: # ensures this is the first particle being added
                    
                    global start_time
                    start_time = time.time() # starts the timer
                    end_time_func(start_time, time_elapsed_label) # calls end_time_func
                

                temp_factor_num = 1.1 # defines temp_factor as 0.01
                particle.move_particle(particles_list, temp_scale.get(), temp_factor_num)

            numofparts_label.config(text=f"Number of particles = {len(particles_list)}")

            # FUNCTION RESPONSIBLE FOR THE INFINITE MOVEMENT OF THE PARTICLES UNLESS CLEARED
            def keep_parts_moving():
                
                turt_can.tracer(0)
                for particle in particles_list: # loops through all of the particles in the list
                    particle.move_particle(particles_list, temp_scale.get(), temp_factor_num) # calls the move_particle method
                turt_can.update() # updates the turtle canvas
                turt_can.tracer(1)
                turt_can.ontimer(keep_parts_moving, 20)

            keep_parts_moving() # calls the keep_parts_moving function


        part_type_button = Button(simulator_win, text="Submit", cursor="hand2") # creates a submit button
        part_type_button.place(x=175, y=48)

        part_num_button = Button(simulator_win, text="Submit", cursor="hand2", command=get_parts) # creates a submit button, when clicked calls the get_parts function
        part_num_button.place(x=150, y=150)

        # FUNCTION RESPONSIBLE FOR CLEARING ALL OF THE CURRENT PARTICLES IN THE TURTLE CANVAS AND RESETTING ALL LIVE STATS TO 0
        def clear_parts():

            for particle in particles_list: # deletes every particle
                particle.hideturtle()
                particle.clear()
                
            particles_list.clear()

            # RESETS ALL THE LIVE STATS TO 0
            numofparts_label.config(text="Number of particles = 0")
            actual_max_speed_label.config(text="Max speed = 0.00 m/s")
            collision_count_label.config(text="Number of collisions = 0")
            time_elapsed_label.config(text=f"Time elapsed = 0.00 s")
            global start_time, end_t, stop_timer
            start_time = None
            end_t = None
            stop_timer = True


        clear_parts_button = Button(simulator_win, text="Clear all particles", command=clear_parts) # creates a button, when clioked clears all particles
        clear_parts_button.place(x=50, y=350)
    
        simulator_goback_button = Button(simulator_win, text="Go Back", cursor="hand2", command=simulator_win.destroy) # creates a go back button
        simulator_goback_button.place(x=50, y=450)


    # FUNCTION RESPONSIBLE FOR THE ABOUT WINDOW
    def about_window():
        
        # CREATING THE ABOUT WINDOW
        about_win = Toplevel(master) # creates a window on top of the home page window for the simulator
        about_win.title("Particle Simulator - About Page") # gives the simulator window a window title
        about_win.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and places it in the middle of the screen
        about_goback_button = Button(about_win, text="Go Back", cursor="hand2", command=about_win.destroy)
        about_goback_button.place(x=50, y=450)
        about_label = Label(about_win, text="The Python file particle_simulator.py is a program that simulates the molecular dynamics of Helium atoms.\n\
                            The atomic weight and radius of this element is taken into consideration when performing calculations.\n\
                            The user can add a variable amount of particles, clear all of the particles and adjust the temperature in K.\n\
                            The root mean square speed (vRMS) formula is applied to Helium to determine the maximum temperature of the particles at the current temperature.\n\
                            The particles collide with both the grey container walls and each other to create a realistic particle simulation.\n\
                            As particles collide with each other, the number of collisions is displayed live.\n\
                            The time elapsed is displayed, which starts counting as soon as the initial particles are added.")
        about_label.place(x=-85, y=175)

    enter_button = Button(master, text="Enter the simulator", font=(15), fg="white", command=simulator_window,
                          cursor = "hand2", activebackground="lightgrey", activeforeground="black", background="seagreen2")
    enter_button.place(x=315, y=200)


    about_button = Button(master, text="About", font=(15), fg="white", padx=52, command=about_window, # creates an options button
                          cursor="hand2", activebackground="lightgrey", activeforeground="black", background="mediumpurple1")
    about_button.place(x=315, y=300) # places the options button in the middle of the screen, below the exit button

    

    master.mainloop() # keeps the home/master window running unless destroyed


home_window() # calls the home_window function to start the program/GUI

    

