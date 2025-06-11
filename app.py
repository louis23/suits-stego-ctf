import streamlit as st
from stegano import lsb
from PIL import Image
import os

# App configuration
st.set_page_config(page_title="Suits Stego CTF", page_icon="🕵️", layout="centered")
st.title("🕵️ Suits Stego Challenge")

# Hidden message
hidden_message = "https://youtu.be/XKxylKR1b-Q?t=110"
encoded_image_path = "suits_encoded.png"
original_image_path = "suits.png"

# Encode image once
if not os.path.exists(encoded_image_path):
    original_image = Image.open(original_image_path).convert("RGB")
    encoded = lsb.hide(original_image, hidden_message)
    encoded.save(encoded_image_path)
    st.success("Image encoded!")

# Display the encoded image
st.image(
    encoded_image_path,
    caption='Decode the hidden URL under the image. Then answer the question: "How much did Louis give Mike as a reward?" Use numbers only, no commas.',
    use_column_width=True
)

# Button to reveal the hidden message
if st.button("🔓 Reveal Hidden Message"):
    revealed = lsb.reveal(encoded_image_path)
    if revealed:
        st.code(revealed)
    else:
        st.error("No hidden message found.")

# --- Answer checking form ---
correct_answer = "10000"  # you can change this if needed

st.markdown("---")
st.subheader("💬 Answer the Question")

with st.form("answer_form"):
    user_answer = st.text_input("What was the reward amount Louis gave Mike?")
    submitted = st.form_submit_button("Submit Answer")

    if submitted:
        # Normalize formatting: remove symbols, commas, lowercase
        normalized = user_answer.strip().replace("$", "").replace(",", "")

        if normalized == correct_answer:
            st.success("✅ Yes, Mike received $10,000 for 'snitching' on Rachel even though he did not have the intention in the first place.")
        else:
            st.warning("❌ Incorrect. Hint: Look at the video at 3:30.")
