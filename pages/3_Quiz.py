import streamlit as st

st.header("It is quiz time 🥳🥳")

q1 = st.selectbox(label="Whats my favorite?", options=["Select one", "Bikes", "Sports", "Games"])

if q1 != "Select one":
    st.write("Ofc It is you dumbhead, none of the options were correct")
    st.image("images/hahahaha.png")

q2 = st.selectbox(label="What is my favorite thing to do?", options=["Select one", "Coding", "Staring at the wall",
                                                                     "Spending time with you"])
if q2 == "Spending time with you":
    st.write("Hehehehehe you guessed it correctly!")
    st.image("images/together.jpeg", width=300)
elif q2 == "Coding":
    st.write("Seriously 😒")
elif q2 == "Staring at the wall":
    st.write("Seriously 😒")

q3 = st.selectbox(label="If I know its the last thing I'd be doin in my life then what would it be?",
                  options=["Select one", "Sky Diving", "Heist", "Go 250+ kmph"])

if q3 != "Select one":
    st.write("I'd love to do all of them but if I were to choose then its gonna be Sky Diving!")
    st.image("images/SkyDive.png")

q4 = st.selectbox(label="What is something which I'll never get tired of doin?",
                  options=("Select one", "Riding my scooty", "Playing games", "Being stupid"))

if q4 != "Select one":
    st.write("Tch Tch you got it wrong again ☹️")
    st.write("Silly, It is ofc kissing you 😛😘")
    st.image("images/K.png")

q5 = st.selectbox(label="Do I like annoying you?",
                  options=["Select one", "Noo", "Never would I ever love to annoy you"])

if q5 != "Select one":
    st.write("Bahahahahhaahahahahahhahaha, I take it as my job to ")
    st.title("Annoy and Irritate you 😈😈")

q6 = st.selectbox(label="What do i play the most?",
                  options=["Select one", "Guitar", "Games", "Basketball"])

if q6 != "Select one":
    st.write("Art..... nah nah I love playing my Guitar more")
    st.image("images/Guitar.png")

q7 = st.selectbox(label="What do I love calling you?",
                  options=["Select one", "My Princess", "My love", "My Vanessa"])

if q7 != "Select one":
    st.write("I'm here to annoy you so😛")
    st.write("I love calling you 'My lil girl' 😝😘")
    col1, col2 = st.columns([0.5, 3])
    with col1:
        st.write("U rn 😂:")
    with col2:
        st.image("images/angy.png")
