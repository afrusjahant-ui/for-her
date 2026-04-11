import streamlit as st

# --- Page Config (Background Color Change) ---
# Nicher code-ta use kore website-er full background ekta light pink color-e change hobe
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffeef2; /* Background Pink */
    }
    /* Ei part-tuku shob lekha kalo korbe */
    h1, h2, h3, p, span, div {
        color: black !important; 
    }
    .stButton>button {
        background-color: #ff8fa3;
        color: white !important; /* Button-er lekha shada thakle bhalo dekhabe */
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title ar Questions ---
st.title("Wanna ask you something honeyyy!😊")
st.subheader("Will you be my wifey?")

# --- Image Placeholder (Ekhane dynamic dynamic GIF asbe) ---
# Amra ekhane shurute shudhu image load korbo
image_placeholder = st.empty() # Khali jayga banay fella

# Prothomei shurur GIF-ta loading message diye load kore rakhi
initial_gif = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHYwdWp3eGZ3eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/4N1wOi78ZGzSB6H7vK/giphy.gif"
image_placeholder.image(initial_gif, caption="Wait, let me look at you first...")


# --- Button Actions ---
col1, col2 = st.columns(2)

with col1:
    if st.button("Yes! ❤️"):
        # Yes chhaple ekhon image ar message shob change hobe
        st.balloons() # Balloons urbe

        # 1. Shurur GIF-ta remove hobe
        image_placeholder.empty()

        # 2. Notun dynamic GIF load hobe (jemon: ekta happy couple ba celebratory GIF)
        celebration_gif = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGM4OWI3NWExODBhYTJmNTllN2NiODBlOTJjMDk1MmRlYzAyZGE2NSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/tP1X48d7cW_9c5vJpE/giphy.gif" # celebration dynamic dynamic GIF link
        st.image(celebration_gif)

        # 3. Notun Success message
        st.success("Yay! ummmmmmahhhh babyyyyyy 💖🥰")


with col2:
    if st.button("No! 💔"):
        st.error("Oops this button is broken! Try the other one")

