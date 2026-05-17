import streamlit as st
import numpy as np
import soundfile as sf
from scipy.io import wavfile

from filters import (
    low_pass_filter,
    high_pass_filter,
    band_pass_filter
)

# PAGE SETTINGS
st.set_page_config(
    page_title="Audio Equalizer",
    layout="centered"
)

# TITLE
st.title("🎵 Audio Equalizer")

st.write("Upload WAV audio and apply filters")

# FILE UPLOADER
uploaded_file = st.file_uploader(
    "Upload WAV File",
    type=["wav"]
)

# IF FILE EXISTS
if uploaded_file is not None:

    # READ AUDIO FILE
    sample_rate, audio_data = wavfile.read(uploaded_file)

    st.success("Audio Uploaded Successfully")

    # PLAY ORIGINAL AUDIO
    st.audio(uploaded_file)

    # FILTER SELECTION
    filter_type = st.selectbox(
        "Select Filter",
        ["Low Pass", "High Pass", "Band Pass"]
    )

    # FREQUENCY SLIDER
    cutoff = st.slider(
        "Cutoff Frequency",
        min_value=100,
        max_value=10000,
        value=2000
    )

    # APPLY FILTER BUTTON
    if st.button("Apply Filter"):

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
        else:

            filtered_audio = band_pass_filter(
                audio_data,
                300,
                cutoff,
                sample_rate
            )

        # CONVERT TO INT16
        filtered_audio = np.int16(filtered_audio)

        # OUTPUT FILE
        output_file = "output.wav"

        # SAVE OUTPUT
        sf.write(
            output_file,
            filtered_audio,
            sample_rate
        )

        st.success("Filter Applied Successfully")

        # PLAY FILTERED AUDIO
        st.audio(output_file)

        # DOWNLOAD BUTTON
        with open(output_file, "rb") as file:

            st.download_button(
                label="Download Filtered Audio",
                data=file,
                file_name="filtered_audio.wav",
                mime="audio/wav"
            )