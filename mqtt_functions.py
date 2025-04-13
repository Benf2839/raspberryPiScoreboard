import paho.mqtt.client as mqtt
from scoreboard_functions import *
# from scoreboard_functions import * # Remove if flash_background is moved or not needed here
import threading # Keep for MQTT loop, remove for clock
import time # Keep for MQTT loop, remove for clock
import tkinter as tk # Keep for tk reference if needed

# Global dictionary to hold references passed from main.py
# This will include StringVars, root, and clock control functions
label_refs = {}



def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to individual topics for each score element
    client.subscribe("tennis/scoreboard/team1_points")
    client.subscribe("tennis/scoreboard/team2_points")
    client.subscribe("tennis/scoreboard/team1_games")
    client.subscribe("tennis/scoreboard/team2_games")
    
    # ... (keep existing subscriptions) ...
    client.subscribe("tennis/scoreboard/clock") # Existing subscription
    client.subscribe("tennis/scoreboard/ball_crossed_line")
    # Control topics
    client.subscribe("tennis/scoreboard/start_clock")
    client.subscribe("tennis/scoreboard/stop_clock")
    client.subscribe("tennis/scoreboard/reset_clock")


def on_message(client, userdata, msg):
    refs = userdata
    payload = msg.payload.decode()
    topic = msg.topic
    print(f"MQTT Message Received Topic: {topic}, Payload: {payload}")

    # --- Handle Score/Label Updates ---
    if topic == "tennis/scoreboard/team1_points":
        # Check if the payload is a valid integer
        var = refs.get("team1_points")
        widget = refs.get("team1_points_widget") # Get the widget reference
        root_ref = refs.get("root")             # Get root reference


        if var:
            var.set(payload)
            # Schedule the flash for the specific widget in the main thread
            if widget and root_ref: # Check if both widget and root exist
                print("Debug: Widget and root exist, scheduling flash...") # Add this
                # Pass the specific widget to flash_widget_bg
                root_ref.after(0, lambda w=widget: multi_flash_widget_bg(w, flash_color="yellow", original_color="lightgray", flashes=3, duration=400))
            else:
                # Add this else block for diagnosis
                print(f"Debug: Flash NOT scheduled. Widget found: {bool(widget)}, Root found: {bool(root_ref)}")

    elif topic == "tennis/scoreboard/team2_points": # <-- Add handler if missing or modify existing
        var = refs.get("team2_points")
        widget = refs.get("team2_points_widget") # <-- Get the specific widget
        if var:
            var.set(payload)
            # Schedule the flash for the specific widget
            if widget and refs.get("root"):
                refs.get("root").after(0, lambda w=widget: multi_flash_widget_bg(w, flash_color="yellow", original_color="lightgray", flashes=3, duration=400))

    elif topic == "tennis/scoreboard/team1_games":
        var_prefix = "var_sets"
        team_suffix = "_team1"
        try:
            games_won, set_number_str = payload.split(",")
            set_number = int(set_number_str)
            var_name = f"{var_prefix}{set_number}{team_suffix}"
            var = refs.get(var_name)
            if var:
                var.set(games_won)
            else:
                print(f"Warning: StringVar '{var_name}' not found in refs.")
        except ValueError:
            print(f"Error parsing team1_games payload: {payload}")
        except KeyError:
             print(f"Warning: Key '{var_name}' not found in refs dictionary.")

    elif topic == "tennis/scoreboard/team2_games":
        var_prefix = "var_sets"
        team_suffix = "_team2"
        try:
            games_won, set_number_str = payload.split(",")
            set_number = int(set_number_str)
            var_name = f"{var_prefix}{set_number}{team_suffix}"
            var = refs.get(var_name)
            if var:
                var.set(games_won)
            else:
                print(f"Warning: StringVar '{var_name}' not found in refs.")
        except ValueError:
            print(f"Error parsing team2_games payload: {payload}")
        except KeyError:
             print(f"Warning: Key '{var_name}' not found in refs dictionary.")


    # --- Handle Clock Updates/Control ---
    elif topic == "tennis/scoreboard/clock":
        try:
            minutes, seconds = map(int, payload.split(':'))
            total_seconds = minutes * 60 + seconds
            set_func = refs.get("set_timer_func")
            if set_func and refs.get("root"):
                refs.get("root").after(0, lambda s=total_seconds: set_func(s))
            else:
                 var = refs.get("clock")
                 if var and refs.get("root"): refs.get("root").after(0, lambda p=payload: var.set(p))
        except ValueError:
            print(f"Error parsing clock payload: {payload}")

    elif topic == "tennis/scoreboard/start_clock":
        start_func = refs.get("start_timer_func")
        if start_func and refs.get("root"):
             refs.get("root").after(0, start_func)

    elif topic == "tennis/scoreboard/stop_clock":
        stop_func = refs.get("stop_timer_func")
        if stop_func and refs.get("root"):
             refs.get("root").after(0, stop_func)

    elif topic == "tennis/scoreboard/reset_clock":
        reset_func = refs.get("reset_timer_func")
        if reset_func and refs.get("root"):
             refs.get("root").after(0, reset_func)

    # --- Other Actions ---
    elif topic == "tennis/scoreboard/ball_crossed_line":
        print("Ball crossed line event received via MQTT")
        # Stuff will be added here later


# Pass the full dictionary as userdata
def connect_to_mqtt(references):
    global label_refs
    label_refs = references # Store all references passed from main

    # Pass references as userdata to callbacks
    client = mqtt.Client(userdata=label_refs)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        # Using standard port 1883 for non-TLS MQTT
        client.connect("benjaminf.net", 1884, 60)
        print("Attempting to connect to MQTT...")
        client.loop_start() # Start network loop in background thread
        return client
    except Exception as e:
        print(f"MQTT Connection Error: {e}")
        return None # Indicate connection failure