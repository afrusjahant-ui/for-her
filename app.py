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
initial_gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjJvZTIzMHB1a2pkZGtsbHFxOGRrMjMyZnhiZzYwNTI2YXBkaXYwdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/901mxGLGQN2PyCQpoc/giphy.gif"
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
    st.success("Yayyyyyy! I knew it.. ummmmmmmahhhh babyyyyyy ❤️🥰")

# --- No Click hole error message dekhabe ---
if no_click:
    st.error("Oops! This button is broken. Try the other one🙈")
