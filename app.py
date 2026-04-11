import streamlit as st

# --- Background ar Styling ---
st.markdown(
    """
    <style>
    .stApp { background-color: #ffeef2; }
    h1, h2, h3, p, span, div { color: black !important; }
    .stButton>button {
        background-color: #ff8fa3;
        color: white !important;
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Top Text Placeholder (Title ar Question-er jonno) ---
text_placeholder = st.empty()
with text_placeholder.container():
    st.title("Wanna ask you something 🥺")
    st.subheader("Will you be my wifey?")

# --- Image Placeholder (GIF-er jonno) ---
image_placeholder = st.empty()
initial_gif = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHYwdWp3eGZ3eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/4N1wOi78ZGzSB6H7vK/giphy.gif"
image_placeholder.image(initial_gif)

# --- Button Placeholder (Button-er jonno) ---
button_placeholder = st.empty()
with button_placeholder.container():
    col1, col2 = st.columns(2)
    with col1:
        yes_click = st.button("Yes! ❤️")
    with col2:
        no_click = st.button("No! 💔")

# --- Yes Click hole shob kisu clear hobe ---
if yes_click:
    # 1. Shob puraton content (Text, GIF, Buttons) vanish kora
    text_placeholder.empty()
    image_placeholder.empty()
    button_placeholder.empty()
    
    # 2. Notun celebration content
    st.balloons()
    # Ekhane ekta celebrate korar moto GIF use kora hoyeche
    new_gif = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW10a213bG0ybGY4a3J1NGRwOGdvd29qdXBvejAzYXA1bWU1ZW4yaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1nUkRa68hPskXLOjIh/giphy.gif"
    st.image(new_gif)
    st.success("Yay! ummmmmmmahhhh babyyyyyy ❤️🥰")

# --- No Click hole error message dekhabe ---
if no_click:
    st.error("Try again! 😜")
