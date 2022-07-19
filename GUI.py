import tkinter as tk
from tkinter import ttk
import Servo as sv
#Colors 
HIGHLIGHT = '#ffffff'
BG = '#05507C'
BUTTON = '#6FC4DB'
DEEP = '#022031'

LARGE_FONT= ("Verdana", 20)

#GUI Inspiration and boiler code courtesy of https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
"""
Some general notes-- this GUI code isnt great-- its very botched. I would love to add an option to have the control values be managed by a PID controller - Jonah
"""
class Simulator_gui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.fig1 = 0
        self.fig2 = 0
        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
            frame.configure(bg = BG)

        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        def SetExperimentValues(self,trial_number, wing_band, force, head_mass, peck_count):
            user_trial = trial_number.get()
            user_wb = wing_band.get()
            user_f = force.get()
            user_mass = head_mass.get()
            user_pc = peck_count.get()
            self.experiment_params ={"Trial" : user_trial, "Wing Band" : user_wb, "Force" : user_f, "Mass" : user_mass, "Number of Pecks" : peck_count}   
            return 0                   
        def RunSimulation(self):
            print(self.experiment_params)
            return False
        def show_plots():
            return False
        def DefaultPeck(self):
            sv.DefaultPeck()
            return 0
        tk.Frame.__init__(self,parent)
        title = tk.Label(self, text="Peck-o-Nator 3000", fg = HIGHLIGHT,bg = BG, font=LARGE_FONT).grid(row = 0,column = 2)
        tk.Label(self,fg =HIGHLIGHT ,bg = BG, text="Trial Number: ", font=("Verdana", 15)).grid(row = 1,column = 1)
        tk.Label(self,fg = HIGHLIGHT,bg = BG, text="Wing Band: ",font=("Verdana", 15)).grid(row = 2,column = 1)
        tk.Label(self,fg = HIGHLIGHT,bg = BG, text="Peck Force (N): ",font=("Verdana", 15)).grid(row = 3,column = 1)
        tk.Label(self,fg = HIGHLIGHT,bg = BG, text="Head Mass (g): ",font=("Verdana", 15)).grid(row = 4,column = 1)
        tk.Label(self,fg = HIGHLIGHT,bg = BG, text="Number of Pecks: ",font=("Verdana", 15)).grid(row = 5,column = 1)
        tk.Label(self, text="", fg = '#FF0000',bg = BG, font= ("Verdana", 6))
        trial_number = tk.Entry(self, width=20,fg = HIGHLIGHT,bg = DEEP)
        trial_number.grid(row = 1,column = 2)
        wing_band = tk.Entry(self, width=20,fg = HIGHLIGHT,bg = DEEP)
        wing_band.grid(row = 2,column = 2)
        force = tk.Entry(self, width=20,fg = HIGHLIGHT,bg = DEEP)
        force.grid(row = 3,column = 2)
        head_mass= tk.Entry(self, width=20,fg = HIGHLIGHT,bg = DEEP)
        head_mass.grid(row = 4,column = 2)
        peck_count = tk.Entry(self, width=20,fg = HIGHLIGHT,bg = DEEP)
        peck_count.grid(row = 5,column = 2)
        confirm = tk.Button(self, text="Confirm Properties",fg = DEEP,bg = BUTTON,
                            command=lambda: SetExperimentValues(self,trial_number, wing_band, force,head_mass)).grid(row = 14, column = 1)
        run = tk.Button(self, text="Run",fg = DEEP,bg = BUTTON,
                            command=lambda: RunSimulation(self)).grid(row = 14, column = 2)
        default_peck = tk.Button(self, text="Default Peck",fg = DEEP,bg = BUTTON,
                            command=lambda: DefaultPeck(self)).grid(row = 14, column = 3)
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
