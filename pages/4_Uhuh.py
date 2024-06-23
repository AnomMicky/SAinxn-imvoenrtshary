import streamlit as st

s1 = st.selectbox(label="Did you finish the quiz?",
             options=["No", "Yes"])

if s1 == "Yes":
    sli = st.slider(label="how annoyed are you rn 😂😂", min_value=0, max_value=10)
    if sli != 0:
        s2 = st.selectbox(label="Do you that you can say INFINITE?", options=["No", "Yes"])
        if s2 == "Yes":
            st.write("Bahahhaha Tooo bad but U can't be that annoyed can you? 😂")
            st.image("images/me.jpeg")
else:
    st.header("Do the quiz first and then come here")