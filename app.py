import streamlit as st

# Page configuration
st.set_page_config(page_title="Special Message", page_icon="💖")

# Title and Question
st.title("Hi! Ekta kotha bolar chilo... 🥰")
st.subheader("Will you be my wifey?")

# Cute GIF (apni চাইলে link change korte paren)
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHY5NjV2ZzR2ZzR2ZzR2ZzR2ZzR2ZzR2ZzR2ZzR2ZzR2ZzR/L40vR0Dk8W3sI/giphy.gif")

# Layout setup
col1, col2 = st.columns(2)

with col1:
    if st.button("Yes! ❤️"):
        st.balloons()
        st.success("Yayyy! I knew it! ummmmahhhhh!alabiuuuuuu 🥰")

with col2:
    if st.button("No 💔"):
        st.error("Error: This button is broken! Try the otherrr one. 😉")
