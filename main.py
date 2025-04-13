import tkinter as tk
from mqtt_functions import *
from scoreboard_functions import *

# --- Setup ---
root = tk.Tk()
root.title("Tennis Scoreboard")
base_width = 1300
base_height = 800
root.geometry(f"{base_width}x{base_height}")
root.configure(bg="darkgreen")

# --- Variables for every white box ---
team1_points = tk.StringVar(value="")
player1_serve = tk.StringVar(value="")
player2_serve = tk.StringVar(value="")
var_match_time = tk.StringVar(value="00:00")
team2_points = tk.StringVar(value="")
player3_serve = tk.StringVar(value="")
player4_serve = tk.StringVar(value="")
var_sets1_team1 = tk.StringVar(value="")
var_sets1_team2 = tk.StringVar(value="")
var_sets2_team1 = tk.StringVar(value="")
var_sets2_team2 = tk.StringVar(value="")
var_sets3_team1 = tk.StringVar(value="")
var_sets3_team2 = tk.StringVar(value="")
var_sets4_team1 = tk.StringVar(value="")
var_sets4_team2 = tk.StringVar(value="")
var_sets5_team1 = tk.StringVar(value="")
var_sets5_team2 = tk.StringVar(value="")
var_match_time = tk.StringVar(value="00:00")

# --- Clock State Variables ---
_timer_running = False
_elapsed_seconds = 0
_after_id = None # To store the id from root.after

# --- Clock Control Functions ---
def format_time(seconds):
    """Formats seconds into MM:SS"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"

def update_timer():
    """Updates the timer display every second if running."""
    global _elapsed_seconds, _after_id, _timer_running
    if _timer_running:
        _elapsed_seconds += 1
        var_match_time.set(format_time(_elapsed_seconds))
        # Schedule the next update
        _after_id = root.after(1000, update_timer)

def start_timer():
    """Starts the timer."""
    global _timer_running
    if not _timer_running:
        print("Starting Timer")
        _timer_running = True
        # Disable Start, Enable Stop/Restart
        btn_start_clock.config(state=tk.DISABLED)
        btn_stop_clock.config(state=tk.NORMAL)
        btn_reset_clock.config(state=tk.NORMAL) # Enable reset button
        update_timer() # Start the update loop

def stop_timer():
    """Stops the timer."""
    global _timer_running, _after_id
    if _timer_running:
        print("Stopping Timer")
        _timer_running = False
        if _after_id:
            root.after_cancel(_after_id)
            _after_id = None
        # Enable Start, Disable Stop
        btn_start_clock.config(state=tk.NORMAL)
        btn_stop_clock.config(state=tk.DISABLED)


def reset_timer():
    """Stops and resets the timer to 00:00."""
    global _elapsed_seconds, _timer_running, _after_id
    print("Resetting Timer")
    if _timer_running:
        stop_timer() # Stop it first if running

    _elapsed_seconds = 0
    var_match_time.set(format_time(_elapsed_seconds))

    # Reset button states
    btn_start_clock.config(state=tk.NORMAL)
    btn_stop_clock.config(state=tk.DISABLED)
    btn_reset_clock.config(state=tk.DISABLED) # Disable reset until started again


# --- Title ---
tk.Label(
    root,
    text="Tennis Scoreboard",
    font=("Helvetica", 32),
    fg="white",
    bg="darkgreen"
).place(relx=650/base_width, rely=30/base_height, anchor="n")  # (0.5, ~0.0375)

# --- Top‑Left: “Points” & two boxes ---
tk.Label(
    root,
    text="Points",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=130/base_width, rely=85/base_height, anchor="nw")

# Big grey box for team1_points
team1_points_label = tk.Label(
    root,
    textvariable=team1_points,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=20,
    height=10
)

team1_points_label.place(relx=100/base_width, rely=130/base_height, anchor="nw")

# Small box & “Player 1”
tk.Label(
    root,
    textvariable=player1_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(relx=300/base_width, rely=160/base_height, anchor="nw")
tk.Label(
    root,
    text="Player 1",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=330/base_width, rely=150/base_height, anchor="nw")

# Small box & “Player 2”
tk.Label(
    root,
    textvariable=player2_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(relx=300/base_width, rely=210/base_height, anchor="nw")
tk.Label(
    root,
    text="Player 2",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=330/base_width, rely=200/base_height, anchor="nw")

# --- Top‑Right: “Sets” using 5 separate boxes ---
tk.Label(
    root,
    text="Sets",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=955/base_width, rely=80/base_height, anchor="nw")

# Individual set boxes for team 1 (top-right)
tk.Label(
    root,
    textvariable=var_sets1_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=795/base_width, rely=150/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets2_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=875/base_width, rely=150/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets3_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=955/base_width, rely=150/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets4_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=1035/base_width, rely=150/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets5_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=1115/base_width, rely=150/base_height, anchor="nw")

# Numbers 1–5 above the boxes
for i in range(5):
    tk.Label(
        root,
        text=str(i+1),
        font=("Helvetica", 16),
        fg="white",
        bg="darkgreen"
    ).place(relx=(830 + i*80)/base_width, rely=120/base_height, anchor="n")

# --- Center: Serve vs Match Time ---
tk.Label(
    root,
    text="Serve",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=270/base_width, rely=330/base_height, anchor="nw")
tk.Label(
    root,
    text="vs",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=370/base_width, rely=330/base_height, anchor="nw")

tk.Label(
    root,
    text="Match Time",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=560/base_width, rely=290/base_height, anchor="nw")

# Create the clock label
tk.Label(
    root,
    textvariable=var_match_time,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=17,
    height=4
).place(relx=575/base_width, rely=330/base_height, anchor="nw")

# --- Bottom‑Left: second big box & players 3/4 ---
team2_points_label=tk.Label(
    root,
    textvariable=team2_points,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=20,
    height=10
)

team2_points_label.place(relx=100/base_width, rely=450/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=player3_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(relx=300/base_width, rely=480/base_height, anchor="nw")
tk.Label(
    root,
    text="Player 3",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=330/base_width, rely=470/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=player4_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(relx=300/base_width, rely=530/base_height, anchor="nw")
tk.Label(
    root,
    text="Player 4",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(relx=330/base_width, rely=520/base_height, anchor="nw")

# --- Bottom‑Right: “1–5” + long sets‑box for team 2 ---
tk.Label(
    root,
    textvariable=var_sets1_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=795/base_width, rely=450/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets2_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=875/base_width, rely=450/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets3_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=955/base_width, rely=450/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets4_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=1035/base_width, rely=450/base_height, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets5_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(relx=1115/base_width, rely=450/base_height, anchor="nw")

for i in range(5):
    tk.Label(
        root,
        text=str(i+1),
        font=("Helvetica", 16),
        fg="white",
        bg="darkgreen"
    ).place(relx=(830 + i*80)/base_width, rely=420/base_height, anchor="n")

# --- Bottom Controls (Buttons) ---
btn_width = 12
btn_height = 2

# -- Clock Control Buttons --
# Place them near the clock display or group them logically
clock_btn_start_x = 180 / base_width
clock_btn_y = 700 / base_height # Place below the clock
clock_btn_spacing = 100 / base_width

btn_start_clock = tk.Button(
    root,
    text="Start",
    width=8, # Smaller width might fit better
    height=btn_height,
    command=start_timer,
    state=tk.NORMAL # Starts enabled
)
btn_start_clock.place(relx=clock_btn_start_x, rely=clock_btn_y)

btn_stop_clock = tk.Button(
    root,
    text="Stop",
    width=8,
    height=btn_height,
    command=stop_timer,
    state=tk.DISABLED # Starts disabled
)
btn_stop_clock.place(relx=clock_btn_start_x + clock_btn_spacing, rely=clock_btn_y)

btn_reset_clock = tk.Button(
    root,
    text="Reset",
    width=8,
    height=btn_height,
    command=reset_timer,
    state=tk.DISABLED # Starts disabled
)
btn_reset_clock.place(relx=clock_btn_start_x + 2*clock_btn_spacing, rely=clock_btn_y)



# -- Other Control Buttons --
other_btn_y = 700 / base_height # Keep original y position
other_btn_start_x = 500 / base_width
other_btn_spacing = 150 / base_width



# Connect to MQTT button
# Note: Pass the actual functions now
btn_connect_mqtt = tk.Button(
    root,
    text="Connect MQTT",
    width=btn_width,
    height=btn_height,
    command=lambda: connect_to_mqtt({
        "team1_points": team1_points,
        "team2_points": team2_points,
        "team1_games": var_sets1_team1,
        "team2_games": var_sets1_team2,
        # --- ADD ALL SET SCORE StringVars ---
        "var_sets1_team1": var_sets1_team1,
        "var_sets1_team2": var_sets1_team2,
        "var_sets2_team1": var_sets2_team1,
        "var_sets2_team2": var_sets2_team2,
        "var_sets3_team1": var_sets3_team1,
        "var_sets3_team2": var_sets3_team2,
        "var_sets4_team1": var_sets4_team1,
        "var_sets4_team2": var_sets4_team2,
        "var_sets5_team1": var_sets5_team1,
        "var_sets5_team2": var_sets5_team2,
        "clock": var_match_time, # Pass the StringVar
        "root": root,
        "team1_points_widget": team1_points_label,
        "team2_points_widget": team2_points_label,
        # --- Pass Clock Control Functions ---
        "start_timer_func": start_timer,
        "stop_timer_func": stop_timer,
        "reset_timer_func": reset_timer,
        "set_timer_func": lambda secs: globals().update({'_elapsed_seconds': secs}) or var_match_time.set(format_time(secs)) # Function to set time directly
    })
)
btn_connect_mqtt.place(relx=other_btn_start_x + other_btn_spacing, rely=other_btn_y)


# Exit Button
btn_exit = tk.Button(
    root,
    text="Exit",
    width=btn_width,
    height=btn_height,
    command=root.quit
)
btn_exit.place(relx=other_btn_start_x + 2*other_btn_spacing, rely=other_btn_y)

# Start the Tkinter main loop
root.mainloop()
