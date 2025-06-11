import streamlit as st
from stegano import lsb
from PIL import Image
import os

st.set_page_config(page_title="Suits Stego CTF", page_icon="🕵️", layout="centered")

st.title("🕵️ Suits Stego Challenge")

# Automatically encode message into the image once, convert image to RGB
if not os.path.exists("suits_encoded.png"):
    hidden_message = "https://youtu.be/XKxylKR1b-Q?t=110"
    original_image = Image.open("suits.png").convert("RGB")
    encoded = lsb.hide(original_image, hidden_message)
    encoded.save("suits_encoded.png")
    st.success("Image encoded!")

# Show image
st.image("suits_encoded.png", caption="Decode the hidden URL under the image. Then answer the question: "How much did Louis give Mike as a reward?", use_column_width=True)

# Button to reveal the message
if st.button("🔓 Reveal Hidden Message"):
    revealed = lsb.reveal("suits_encoded.png")
    if revealed:
        st.code(revealed)
    else:
        st.error("No hidden message found.")
