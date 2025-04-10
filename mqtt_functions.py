import paho.mqtt.client as mqtt
from scoreboard_functions import *
import threading
import time
import tkinter as tk

# Global label references (passed through userdata in connect_to_mqtt)
label_refs = {}

# Clock control
clock_running = False
clock_seconds = 0
clock_thread = None


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to individual topics for each score element
    client.subscribe("tennis/scoreboard/team1_points")
    client.subscribe("tennis/scoreboard/team2_points")
    client.subscribe("tennis/scoreboard/team1_games")
    client.subscribe("tennis/scoreboard/team2_games")
    client.subscribe("tennis/scoreboard/set")
    client.subscribe("tennis/scoreboard/clock")
    client.subscribe("tennis/scoreboard/ball_crossed_line")
    client.subscribe("tennis/scoreboard/start_clock")
    client.subscribe("tennis/scoreboard/stop_clock")
    client.subscribe("tennis/scoreboard/reset_clock")  # Add subscription for reset clock


def format_clock(seconds):
    minutes = seconds // 60
    sec = seconds % 60
    return f"{minutes}:{sec:02d}"

def clock_updater():
    global clock_seconds, clock_running
    while clock_running:
        time.sleep(1)
        clock_seconds += 1
        if "clock" in label_refs:
            label_refs["clock"].config(text=format_clock(clock_seconds))

def start_clock():
    global clock_running, clock_thread
    if not clock_running:
        clock_running = True
        clock_thread = threading.Thread(target=clock_updater, daemon=True)
        clock_thread.start()

def stop_clock():
    global clock_running
    clock_running = False

def reset_clock():
    global clock_seconds
    clock_seconds = 0  # Reset the clock to 0 seconds
    if "clock" in label_refs:
        label_refs["clock"].config(text=format_clock(clock_seconds))  # Update the label to show "0:00"
    stop_clock()  # Optionally stop the clock after reset

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"MQTT Message: {payload}")

    if msg.topic == "tennis/scoreboard/team1_points":
        if "team1_points" in label_refs:
            label_refs["team1_points"].set(payload)

    elif msg.topic == "tennis/scoreboard/team2_points":
        if "team2_points" in label_refs:
            label_refs["team2_points"].set(payload)

    elif msg.topic == "tennis/scoreboard/team1_games":
        if "team1_games" in label_refs:
            # Expecting payload format: "games_won,set_number" (e.g., "3,1")
            games_won, set_number = payload.split(",")
            set_number = int(set_number)
            # Now update the appropriate label for the set
            if set_number == 1:
                label_refs["var_sets1_team1"].set(games_won)
            elif set_number == 2:
                label_refs["var_sets2_team1"].set(games_won)
            elif set_number == 3:
                label_refs["var_sets3_team1"].set(games_won)
            elif set_number == 4:
                label_refs["var_sets4_team1"].set(games_won)
            elif set_number == 5:
                label_refs["var_sets5_team1"].set(games_won)

    elif msg.topic == "tennis/scoreboard/team2_games":
        if "team2_games" in label_refs:
            # Expecting payload format: "games_won,set_number" (e.g., "2,1")
            games_won, set_number = payload.split(",")
            set_number = int(set_number)
            # Now update the appropriate label for the set
            if set_number == 1:
                label_refs["var_sets1_team2"].set(games_won)
            elif set_number == 2:
                label_refs["var_sets2_team2"].set(games_won)
            elif set_number == 3:
                label_refs["var_sets3_team2"].set(games_won)
            elif set_number == 4:
                label_refs["var_sets4_team2"].set(games_won)
            elif set_number == 5:
                label_refs["var_sets5_team2"].set(games_won)

    elif msg.topic == "tennis/scoreboard/set":
        if "set" in label_refs:
            label_refs["set"].set(f"Set: {payload}")

    elif msg.topic == "tennis/scoreboard/clock":
        if "clock" in label_refs:
            label_refs["clock"].set(payload)

        # Reset internal clock counter to match the given time
        minutes, seconds = map(int, payload.split(":"))
        global clock_seconds
        clock_seconds = minutes * 60 + seconds

    elif msg.topic == "tennis/scoreboard/ball_crossed_line":
        flash_background(label_refs.get("root"))  # flash the root window

    elif msg.topic == "tennis/scoreboard/start_clock":
        print("Clock started via MQTT")
        start_clock()

    elif msg.topic == "tennis/scoreboard/stop_clock":
        print("Clock stopped via MQTT")
        stop_clock()

    elif msg.topic == "tennis/scoreboard/reset_clock":
        print("Clock reset via MQTT")
        reset_clock()  # Call reset clock function when receiving the reset_clock message


# Updated connect_to_mqtt with userdata argument for passing label references
def connect_to_mqtt(label_references):
    global label_refs
    label_refs = label_references  # Set label references globally

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("benjaminf.net", 1884, 60)  # Using the domain name instead of direct server IP
    client.loop_start()
    return client
