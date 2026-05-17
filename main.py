import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from scipy.io import wavfile
import numpy as np
import pygame

from filters import (
    low_pass_filter,
    high_pass_filter,
    band_pass_filter
)

# GLOBAL VARIABLES
audio_data = None
sample_rate = None
output_file = "output.wav"

# -----------------------------
# LOAD AUDIO FILE
# -----------------------------
def load_audio():

    global audio_data
    global sample_rate

    file_path = filedialog.askopenfilename(
        filetypes=[("WAV Files", "*.wav")]
    )

    if file_path:

        sample_rate, audio_data = wavfile.read(file_path)

        messagebox.showinfo(
            "Success",
            "Audio Loaded Successfully"
        )

# -----------------------------
# APPLY FILTER
# -----------------------------
def apply_filter():

    global audio_data
    global sample_rate

    if audio_data is None:

        messagebox.showerror(
            "Error",
            "Please Upload Audio First"
        )

        return

    filter_type = filter_var.get()

    cutoff = cutoff_slider.get()

    # LOW PASS
    if filter_type == "Low Pass":

        filtered_audio = low_pass_filter(
            audio_data,
            cutoff,
            sample_rate
        )

    # HIGH PASS
    elif filter_type == "High Pass":

        filtered_audio = high_pass_filter(
            audio_data,
            cutoff,
            sample_rate
        )

    # BAND PASS
    elif filter_type == "Band Pass":

        filtered_audio = band_pass_filter(
            audio_data,
            300,
            cutoff,
            sample_rate
        )

    else:
        return

    # CONVERT TO 16-BIT
    filtered_audio = np.int16(filtered_audio)

    # SAVE OUTPUT
    wavfile.write(
        output_file,
        sample_rate,
        filtered_audio
    )

    messagebox.showinfo(
        "Completed",
        "Filter Applied Successfully"
    )

# -----------------------------
# PLAY FILTERED AUDIO
# -----------------------------
def play_audio():

    try:

        pygame.mixer.init()

        pygame.mixer.music.load(output_file)

        pygame.mixer.music.play()

    except:

        messagebox.showerror(
            "Error",
            "Please Apply Filter First"
        )

# -----------------------------
# GUI WINDOW
# -----------------------------
root = tk.Tk()

root.title("Audio Equalizer GUI")

root.geometry("450x450")

root.config(bg="#1e1e1e")

# TITLE
title = tk.Label(
    root,
    text="Audio Equalizer",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=20)

# LOAD BUTTON
load_button = tk.Button(
    root,
    text="Upload WAV File",
    command=load_audio,
    width=20,
    height=2,
    bg="#4CAF50",
    fg="white"
)

load_button.pack(pady=10)

# FILTER DROPDOWN
filter_var = tk.StringVar()

filter_var.set("Low Pass")

filters = [
    "Low Pass",
    "High Pass",
    "Band Pass"
]

dropdown = tk.OptionMenu(
    root,
    filter_var,
    *filters
)

dropdown.config(
    width=20,
    bg="#2196F3",
    fg="white"
)

dropdown.pack(pady=20)

# CUTOFF SLIDER
cutoff_slider = tk.Scale(
    root,
    from_=100,
    to=10000,
    orient="horizontal",
    length=300,
    label="Cutoff Frequency",
    bg="#1e1e1e",
    fg="white"
)

cutoff_slider.pack(pady=20)

# APPLY BUTTON
apply_button = tk.Button(
    root,
    text="Apply Filter",
    command=apply_filter,
    width=20,
    height=2,
    bg="#FF9800",
    fg="white"
)

apply_button.pack(pady=10)

# PLAY BUTTON
play_button = tk.Button(
    root,
    text="Play Output Audio",
    command=play_audio,
    width=20,
    height=2,
    bg="#9C27B0",
    fg="white"
)

play_button.pack(pady=10)

# EXIT BUTTON
exit_button = tk.Button(
    root,
    text="Exit",
    command=root.quit,
    width=20,
    height=2,
    bg="#f44336",
    fg="white"
)

exit_button.pack(pady=20)

# START GUI
root.mainloop()