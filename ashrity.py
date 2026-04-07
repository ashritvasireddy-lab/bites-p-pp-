import streamlit as st

st.title("📐 Rectangle Calculator")

# Input fields without min_value or step
length = st.number_input("Enter the length:")
width = st.number_input("Enter the width:")

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

st.subheader("Results")
st.write("Your area is", area)
st.write("Your perimeter is", perimeter)
