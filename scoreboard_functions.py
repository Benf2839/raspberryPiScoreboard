from time import time

# Initialize global variables
start_time = None
team1_points = 0
team2_points = 0
team1_games = 0
team2_games = 0
team1_sets = 0
team2_sets = 0

# Tennis scoring format
point_labels = ["0", "15", "30", "40"]

# Update the score on the scoreboard
def update_score(score_label, team1_points, team2_points):
    score_label.config(text=f"Team 1: {point_labels[team1_points]} - Team 2: {point_labels[team2_points]}")

# Flash the red background on the window (only 3 times)
flash_count = 0
def flash_background(root):
    global flash_count
    if flash_count < 3:
        current_color = root.cget("bg")
        new_color = "red" if current_color == "white" else "white"
        root.config(bg=new_color)
        flash_count += 1
        root.after(500, flash_background, root)  # Flash every 500 ms

# Update the play clock
def update_clock(clock_var, start_time):
    elapsed_time = time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    clock_var.set(f"{minutes:02}:{seconds:02}")  # Update the StringVar with formatted time
    clock_var.get()  # This call ensures that the value is set, but it's not necessary to store the return value
    return clock_var  # Just to maintain function structure, you could also omit this

# Function to start the play clock when the "Start Clock" button is pressed
def start_play_clock(clock_var):
    global start_time
    start_time = time()
    update_clock(clock_var, start_time)
