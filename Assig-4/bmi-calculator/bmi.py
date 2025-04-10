import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg.")
height = st.number_input("Enter your height in cm.")

if st.button("Calculate BMI"):
    final_height = (height / 100) ** 2  # Convert cm to meters
    bmi = weight / final_height
    st.success(f'Your BMI is: {bmi:.2f}')

    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight")
    elif 25 <= bmi < 29.9:
        st.info("Overweight")
    else:
        st.error("Obesity")
