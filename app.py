import streamlit as st
from stegano import lsb
from PIL import Image
import os

st.set_page_config(page_title="Suits Stego CTF", page_icon="🕵️", layout="centered")

st.title("🕵️ Suits Stego Challenge")

# Automatically encode message into the image once
if not os.path.exists("suits_encoded.png"):
    hidden_message = "https://youtu.be/XKxylKR1b-Q?t=110"
    encoded = lsb.hide("suits.png", hidden_message)
    encoded.save("suits_encoded.png")
    st.success("Image encoded!")

# Show image
st.image("suits_encoded.png", caption="Decode me if you can 🕵️", use_column_width=True)

# Button to reveal the message
if st.button("🔓 Reveal Hidden Message"):
    revealed = lsb.reveal("suits_encoded.png")
    if revealed:
        st.code(revealed)
    else:
        st.error("No hidden message found.")
