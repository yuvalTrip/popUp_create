import tkinter as tk
import game
popup = None  # Define popup as a global variable

def start_game(people_entry, angle_entry,recognize_entry,pdecrease_entry,ttime_entry):
    num_people = int(people_entry.get())
    angle_sun = int(angle_entry.get())
    recognize_points=int(recognize_entry.get())
    decrease_points=int(pdecrease_entry.get())
    totaltime=int(ttime_entry.get())
    game.start_game(num_people, angle_sun,recognize_points,decrease_points,totaltime)#send values to different class- we want it to be json
    popup.destroy()  # Close the popup window

def create_popup():
    global popup  # Use the global popup variable

    popup = tk.Tk()
    popup.title("Game Settings")

    # Label and Entry for Number of People
    people_label = tk.Label(popup, text="Number of People:")
    people_label.grid(row=0, column=0)
    people_entry = tk.Entry(popup)
    people_entry.grid(row=0, column=1)

    # Label and Entry for Angle of Sun
    angle_label = tk.Label(popup, text="Angle of Sun:")
    angle_label.grid(row=1, column=0)
    angle_entry = tk.Entry(popup)
    angle_entry.grid(row=1, column=1)

    # Label and Entry for points increase for recognizing people
    recognize_label = tk.Label(popup, text="Points increase for recognizing people:")
    recognize_label.grid(row=2, column=0)
    recognize_entry = tk.Entry(popup)
    recognize_entry.grid(row=2, column=1)

    # Label and Entry for points decrease per minute
    pdecrease_label = tk.Label(popup, text="Points decrease per minute:")
    pdecrease_label.grid(row=3, column=0)
    pdecrease_entry = tk.Entry(popup)
    pdecrease_entry.grid(row=3, column=1)

    # Label and Entry for simulation total time
    ttime_label = tk.Label(popup, text="Simulation total time:")
    ttime_label.grid(row=4, column=0)
    ttime_entry = tk.Entry(popup)
    ttime_entry.grid(row=4, column=1)

    # Button to Start Game
    start_button = tk.Button(popup, text="Start Game", command=lambda: start_game(people_entry, angle_entry,recognize_entry,pdecrease_entry,ttime_entry))
    start_button.grid(row=5, columnspan=2)

    popup.mainloop()

if __name__ == "__main__":
    create_popup()
