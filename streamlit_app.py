import streamlit as st
import pickle

model = pickle.load(open('Naive_bayes1.pkl', 'rb'))

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title('ML Model')
st.header('Email_spam_detection')

user_input = st.text_input('Enter a Message')

if user_input:
    prediction = model.predict([user_input])
    st.write(f"The prediction result is:" )
    if prediction == 0:
        st.write('The mail is Spam')
    else:
        st.write("The mail is not Spam")