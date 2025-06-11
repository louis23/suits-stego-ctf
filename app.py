import streamlit as st
from stegano import lsb
from PIL import Image
from io import BytesIO

# XOR encryption/decryption
def xor_encrypt_decrypt(message, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))

# Accepted variants of the answer
accepted_answers = ["10000", "10,000", "10k", "10K"]

# Streamlit UI setup
st.set_page_config(page_title="Suits Stego CTF", page_icon="🕵️", layout="centered")
st.title("🕵️ Suits Steganography Challenge")

# Step 1: Show the video
st.markdown("### 🎥 Step 1: Watch the Video")
st.video("https://youtu.be/XKxylKR1b-Q?t=110")
st.info("Find out how much Louis gave Mike as a reward.")

# Step 2: Encode the answer
st.markdown("### 🧩 Step 2: Encode the Answer into the Image")
st.image("suits.png", caption="Base Image – Hide your answer under this image", use_container_width=True)

user_message = st.text_input("Enter the secret message you want to hide:")
encode_key = st.text_input("Enter a key to encrypt your message:")

if st.button("🔐 Encode"):
    if user_message and encode_key:
        try:
            encrypted = xor_encrypt_decrypt(user_message, encode_key)
            original = Image.open("suits.png").convert("RGB")
            encoded = lsb.hide(original, encrypted)

            buffer = BytesIO()
            encoded.save(buffer, format="PNG")
            buffer.seek(0)

            st.image(buffer, caption="🔏 Encoded Image", use_container_width=True)
            st.success("✅ Image encoded! Now try decoding it below.")

            st.download_button(
                label="📥 Download Encoded Image (PNG)",
                data=buffer,
                file_name="encoded_image.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"Error during encoding: {e}")
    else:
        st.warning("Please enter both a message and an encryption key.")

# Step 3: Decode the hidden message
st.markdown("### 🕵️ Step 3: Decode the Hidden Message")
uploaded_file = st.file_uploader("Upload the encoded image (PNG)", type=["png"])
decode_key = st.text_input("Enter the decryption key:")

if st.button("🔓 Decode"):
    if uploaded_file and decode_key:
        try:
            image = Image.open(uploaded_file)
            hidden = lsb.reveal(image)
            if hidden:
                decrypted = xor_encrypt_decrypt(hidden, decode_key.strip())
                st.code(decrypted)
                if decrypted.strip().lower() in [ans.lower() for ans in accepted_answers]:
                    st.success("✅ Great job! You have successfully encoded and decoded the hidden message.")
                else:
                    st.warning("❌ Incorrect message. Hint: Look at the video at 3:30.")
            else:
                st.error("No hidden message found.")
        except Exception as e:
            st.error(f"Error during decoding: {e}")
    else:
        st.warning("Please upload an image and enter the decryption key.")

# import streamlit as st
# from stegano import lsb
# from PIL import Image
# import os

# # App configuration
# st.set_page_config(page_title="Suits Stego CTF", page_icon="🕵️", layout="centered")
# st.title("🕵️ Suits Stego Challenge")

# st.markdown("""
# Welcome to the **Steganography Challenge**! 🕵️  
# An image can hide **secret messages** in plain sight. Your mission is to:
# 1. **Find the hidden message** in the image below.
# 2. **Follow the clue**.
# 3. **Answer the question correctly** to reveal the final secret!

# ---

# **Steganography** is the practice of hiding data in other files like images, audio, or video. Let's dive in! 🔍
# """)
# # Hidden message
# hidden_message = "https://youtu.be/XKxylKR1b-Q?t=110"
# encoded_image_path = "suits_encoded.png"
# original_image_path = "suits.png"

# # Encode image once
# if not os.path.exists(encoded_image_path):
#     original_image = Image.open(original_image_path).convert("RGB")
#     encoded = lsb.hide(original_image, hidden_message)
#     encoded.save(encoded_image_path)
#     st.success("Image encoded!")

# # Display the encoded image
# st.image(
#     encoded_image_path,
#     caption='Decode the hidden URL under the image. Then answer the question: "How much did Louis give Mike as a reward?" Use numbers only, no commas.',
#     use_container_width=True
# )

# # Button to reveal the hidden message
# if st.button("🔓 Reveal Hidden Message"):
#     revealed = lsb.reveal(encoded_image_path)
#     if revealed:
#         st.code(revealed)
#     else:
#         st.error("No hidden message found.")

# # --- Answer checking form ---
# correct_answer = "10000"  # you can change this if needed

# st.markdown("---")
# st.subheader("💬 Answer the Question")

# with st.form("answer_form"):
#     user_answer = st.text_input("What was the reward amount Louis gave Mike?")
#     submitted = st.form_submit_button("Submit Answer")

#     if submitted:
#         # Normalize formatting: remove symbols, commas, lowercase
#         normalized = user_answer.strip().replace("$", "").replace(",", "")

#         if normalized == correct_answer:
#             st.success("✅ Yes, Mike received $10,000 for 'snitching' on Rachel even though he did not have the intention in the first place.")
#         else:
#             st.warning("❌ Incorrect. Hint: Look at the video at 3:30.")



