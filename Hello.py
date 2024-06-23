import streamlit as st

st.set_page_config('wide')

col1, col2 = st.columns([2, 0.5])

with col1:
    st.header("Hello there, Miss Gorgeous!!")
with col2:
    st.image("images/greet.png")

st.subheader("You must be wondering why you are here?")
st.write("Or do you already know it by now? 🤔")
st.write("I love you is what I want you to know 🤭")

content = """Before we move ahead, I'd like to give you instructions on how you 
            are supposed to navigate here, to your left you would seeing a list 
            things where you will be finding different things (I have no clue
            what and all will be there, it is a surprise for me as well lol(i mean
            im writing this before making anything)), U can go to whatever u feel like 
            reading first, they wont be having an connection between them prolly.
            
            before moving on answer the below question 🥺
            """
st.info(content)

select = st.selectbox(label="Are you still Angy on me?☹️", placeholder="Yes or No 🥺", options=["☹️", "Yes 😠", "NO"])
col3, col4 = st.columns([2, 1.5])
if select == "Yes 😠":
    with col3:
        st.image("images/sad.jpeg", width=400)
    with col4:
        st.subheader("I'm sorry 🥺, please forgive me")
        st.write("I will never do it again, pakka promise!")
        st.write("Now u can look to your left to find everything else 🤭")
        st.image("images/unfold.png", width=200)
    st.write("I'm not good at making websites at all 😓, I'm trying my best")
elif select == "NO":
    with col3:
        st.image("images/together.jpeg")
    with col4:
        st.subheader("I'm sorry for doin it 🥺")
        st.write("I will never repeat it again, Pinky promise!")
        st.write("Now u can look to your left to find everything else 🤭")
        st.image("images/unfold.png", width=200)
    st.write("I'm not good at making websites at all 😓, I'm trying my best")
