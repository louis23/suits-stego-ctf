
# 🕵️ Suits & Steganography Challenge

A fun and beginner-friendly cybersecurity CTF-style project using steganography and Streamlit — inspired by a scene from the TV show *Suits*. This project lets users hide a secret message inside an image, encrypt it with a custom key (and optionally base64 encode it), then attempt to decode it later using the correct decryption key.

App: https://suits-stego-ctf.streamlit.app/

<img width="781" height="861" alt="Screenshot 2025-07-14 at 10 16 31 PM" src="https://github.com/user-attachments/assets/d194cb93-9e56-4bf6-a73a-bbc7f3ae8db8" />


## 🎯 Objective

- Watch the **Suits** video clip.
- Find the **reward amount** Louis gave Mike.
- Embed this answer into an image using encryption and optional Base64.
- Attempt to **decode the hidden message** with the correct decryption key.
- Receive a success message only if the hidden message is correctly decrypted and matches the expected answer.

---

## 🚀 Features

| Feature                       | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 🔐 Encode Message             | Encrypt your message using a key, and hide it inside an image using LSB.   |
| 📥 Download Encoded Image    | Save your stego image locally for submission or challenge sharing.         |
| 🕵️ Decode Message             | Upload an encoded image and decrypt the hidden message using your key.     |
| ✅ Answer Validation          | Match the decrypted message against multiple accepted formats.             |
| 🔁 Optional Base64 Encoding   | Toggle Base64 encoding before embedding.                                    |
| 📱 Mobile-Compatible Video   | Video link with a clickable thumbnail for better mobile support.            |

---

## 🧪 Tech Stack

- [Streamlit](https://streamlit.io/) - for the web app interface
- [Stegano](https://pypi.org/project/stegano/) - for LSB steganography
- [Pillow](https://pillow.readthedocs.io/) - image processing
- Python standard libraries
