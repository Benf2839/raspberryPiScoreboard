from time import time
import tkinter as tk

# Initialize global variables
start_time = None
team1_points = 0
team2_points = 0
team1_games = 0
team2_games = 0
team1_sets = 0
team2_sets = 0
flash_count = 0 
start_time = "00:00"  # Initialize start_time to a default value


# --- Function to flash a specific widget's background ---
def flash_widget_bg(widget, flash_color="yellow", original_color="lightgray", duration=150):
    """Temporarily changes the background color of a specific widget."""
    if widget:
        try:
            # Change to flash color
            widget.config(bg=flash_color)
            # Schedule reverting back to original color after 'duration' milliseconds
            widget.after(duration, lambda: widget.config(bg=original_color))
        except tk.TclError:
            # Handle potential error if widget is destroyed before callback
            print(f"Warning: Could not configure widget {widget}")


def multi_flash_widget_bg(widget, flash_color="yellow", original_color="lightgray", flashes=3, duration=120):
    """
    Flashes the widget background multiple times.
    'flashes' is the number of times it should turn ON (e.g., 3).
    Total state changes will be flashes * 2.
    """
    if not widget: # Safety check
        return

    # Calculate total steps (on/off cycles)
    total_steps = flashes * 2

    def toggle_flash(step_count):
        """Inner function to handle recursive toggling."""
        if step_count <= 0:
            # Ensure it ends on the original color
            try:
                widget.config(bg=original_color)
            except tk.TclError:
                 print(f"Warning: Could not configure widget {widget} at end of flash.")
            return # Stop the recursion

        # Determine current color state for toggle
        # Even steps remaining = turn OFF (set to original)
        # Odd steps remaining = turn ON (set to flash)
        next_color = original_color if (step_count % 2 == 0) else flash_color

        try:
            widget.config(bg=next_color)
            # Schedule the next toggle
            widget.after(duration, lambda: toggle_flash(step_count - 1))
        except tk.TclError:
            print(f"Warning: Could not configure widget {widget} during flash step {step_count}.")
            # Attempt to reset to original if error occurs mid-flash
            try: widget.config(bg=original_color)
            except tk.TclError: pass # Ignore if already destroyed

    # --- Start the flashing sequence ---
    # We start with an odd number of steps if total_steps is odd,
    # ensuring the first action is to turn ON.
    # If the widget isn't currently the original color, force it first (optional but safer)
    try:
        if widget.cget("bg") != original_color:
            widget.config(bg=original_color)
        # Start the toggling process
        toggle_flash(total_steps)
    except tk.TclError:
        print(f"Warning: Could not configure widget {widget} at start of flash.")



def start_play_clock(clock_label, root):
    global start_time
    start_time = time()
    update_clock_auto(clock_label, root)

def update_clock_auto(clock_label, root):
    global start_time
    elapsed_time = time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    clock_label.config(text=f"{minutes:02}:{seconds:02}")
    root.after(1000, update_clock_auto, clock_label, root)

