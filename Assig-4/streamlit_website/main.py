import streamlit as st 

st.set_page_config(page_title="My first website",page_icon="🌐", layout="centered")
st.title("Welcome to my first python website.")

st.sidebar.title("Navigation")
page= st.sidebar.radio("Go to", ["Home","About","Contact"])

if page == "Home":
    st.header("Home page")
    st.write("This is a simple home page buit with python and streamlit")
    name = st.text_input("What\'s your name?")
    if name:
        st.success(f'Hello {name}! Thnaks for visiting.')

elif page == "About":
    st.header("About page")
    st.write("This website is built entirely using python and streamlit in under 15 minuts!")

elif page == "Contact":
    st.header("Contact Us")
    email = st.text_input("Your email")
    message = st.text_input("Your message.")
    if st.button("Submit"): 
        st.success("Thank you! We have received your message.")   
