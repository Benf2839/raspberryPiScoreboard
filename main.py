import tkinter as tk
from mqtt_functions import *
from scoreboard_functions import *

# ——— Setup ———
root = tk.Tk()
root.title("Tennis Scoreboard")
root.geometry("1300x800")
root.configure(bg="darkgreen")

# ——— Variables for every white box ———
team1_points = tk.StringVar(value="")
player1_serve = tk.StringVar(value="")
player2_serve = tk.StringVar(value="")
var_sets1 = tk.StringVar(value="")
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

# ——— Title ———
tk.Label(
    root,
    text="Tennis Scoreboard",
    font=("Helvetica", 32),
    fg="white",
    bg="darkgreen"
).place(x=650, y=30, anchor="n")

# ——— Top‑Left: “Points” & two boxes ———
tk.Label(
    root,
    text="Points",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=130, y=85, anchor="nw")

# Big grey box for team1_points
tk.Label(
    root,
    textvariable=team1_points,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=20,
    height=10
).place(x=100, y=130, anchor="nw")

# Small box & “Player 1”
tk.Label(
    root,
    textvariable=player1_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(x=300, y=160, anchor="nw")
tk.Label(
    root,
    text="Player 1",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=330, y=150, anchor="nw")

# Small box & “Player 2”
tk.Label(
    root,
    textvariable=player2_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(x=300, y=210, anchor="nw")
tk.Label(
    root,
    text="Player 2",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=330, y=200, anchor="nw")

# ——— Top‑Right: “Sets” using 5 separate boxes ———
tk.Label(
    root,
    text="Sets",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=955, y=80, anchor="nw")

# Individual set boxes for team 1 (top-right)
tk.Label(
    root,
    textvariable=var_sets1_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=795, y=150, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets2_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=875, y=150, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets3_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=955, y=150, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets4_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=1035, y=150, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets5_team1,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=1115, y=150, anchor="nw")

# Numbers 1–5 above the boxes
for i in range(5):
    tk.Label(
        root,
        text=str(i+1),
        font=("Helvetica", 16),
        fg="white",
        bg="darkgreen"
    ).place(x=830 + i*80, y=120, anchor="n")

# ——— Center: Serve vs Match Time ———
tk.Label(
    root,
    text="Serve",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=270, y=330, anchor="nw")
tk.Label(
    root,
    text="vs",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=370, y=330, anchor="nw")

tk.Label(
    root,
    text="Match Time",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=560, y=290, anchor="nw")
# Create the clock label with the StringVar
clock_label = tk.Label(
    root,
    textvariable=var_match_time,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=17,
    height=4
).place(x=575, y=330, anchor="nw")

# ——— Bottom‑Left: second big box & players 3/4 ———
tk.Label(
    root,
    textvariable=team2_points,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=20,
    height=10
).place(x=100, y=450, anchor="nw")

tk.Label(
    root,
    textvariable=player3_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(x=300, y=480, anchor="nw")
tk.Label(
    root,
    text="Player 3",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=330, y=470, anchor="nw")

tk.Label(
    root,
    textvariable=player4_serve,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=2,
    height=1
).place(x=300, y=530, anchor="nw")
tk.Label(
    root,
    text="Player 4",
    font=("Helvetica", 20),
    fg="white",
    bg="darkgreen"
).place(x=330, y=520, anchor="nw")

# ——— Bottom‑Right: “1–5” + long sets‑box ———
tk.Label(
    root,
    textvariable=var_sets1_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=795, y=450, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets2_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=875, y=450, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets3_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=955, y=450, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets4_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=1035, y=450, anchor="nw")

tk.Label(
    root,
    textvariable=var_sets5_team2,
    bg="lightgray",
    bd=2,
    relief="solid",
    width=10,
    height=7
).place(x=1115, y=450, anchor="nw")

for i in range(5):
    tk.Label(
        root,
        text=str(i+1),
        font=("Helvetica", 16),
        fg="white",
        bg="darkgreen"
    ).place(x=830 + i*80, y=420, anchor="n")

# ——— Bottom Controls (Buttons) ———
btn_width = 12
btn_height = 2

# Start Play Clock
tk.Button(
    root,
    text="Start Clock",
    width=btn_width,
    height=btn_height,
    command=start_play_clock
).place(x=200, y=700)

# Flash Background
tk.Button(
    root,
    text="Flash",
    width=btn_width,
    height=btn_height,
    command=lambda: flash_background(root)
).place(x=500, y=700)

# Connect to MQTT
tk.Button(
    root,
    text="Connect MQTT",
    width=12,
    height=2,
    command=lambda: connect_to_mqtt({
        "team1_points": team1_points,
        "team2_points": team2_points,
        "team1_set1_games": var_sets1_team1,
        "team2_set1_games": var_sets1_team2,
        "team1_set2_games": var_sets2_team1,
        "team2_set2_games": var_sets2_team2,
        "team1_set3_games": var_sets3_team1,
        "team2_set3_games": var_sets3_team2,
        "team1_set4_games": var_sets4_team1,
        "team2_set4_games": var_sets4_team2,
        "team1_set5_games": var_sets5_team1,
        "team2_set5_games": var_sets5_team2,
        "set": var_sets1,
        "clock": var_match_time,
        "root": root
    })
).place(x=650, y=700)

# Exit Button
tk.Button(
    root,
    text="Exit",
    width=btn_width,
    height=btn_height,
    command=root.quit
).place(x=800, y=700)

# Start the Tkinter main loop
root.mainloop()
