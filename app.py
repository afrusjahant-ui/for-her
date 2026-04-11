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

st.title("Hi! Ekta kotha bolar chilo... 😊")

# --- Image Placeholder (GIF er jonno) ---
image_placeholder = st.empty()
initial_gif = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHYwdWp3eGZ3eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/4N1wOi78ZGzSB6H7vK/giphy.gif"
image_placeholder.image(initial_gif)

st.subheader("Will you be my wifey?")

# --- Button Placeholder (Eitai button soraye felbe) ---
button_placeholder = st.empty()

# Button gulo ke ekta container-e rakhlam
with button_placeholder.container():
    col1, col2 = st.columns(2)
    with col1:
        yes_click = st.button("Yes! ❤️")
    with col2:
        no_click = st.button("No! 💔")

# --- Yes Click hole ki hobe ---
if yes_click:
    # 1. Button ar shurur GIF soraye fela
    button_placeholder.empty()
    image_placeholder.empty()
    
    # 2. Notun GIF ebong Balloons
    st.balloons()
    new_gif = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGM4OWI3NWExODBhYTJmNTllN2NiODBlOTJjMDk1MmRlYzAyZGE2NSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/tP1X48d7cW_9c5vJpE/giphy.gif"
    st.image(new_gif)
    st.success("Yay! ummmmmmmahhhh babyyyyyy ❤️🥰")

# --- No Click hole ki hobe ---
if no_click:
    st.error("Try again! 😜")
