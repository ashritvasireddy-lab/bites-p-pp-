import streamlit as st

st.title("📐 Rectangle Calculator")

# Input fields
length = st.number_input("Enter the length:", min_value=0.0, step=0.1)
width = st.number_input("Enter the width:", min_value=0.0, step=0.1)

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

st.subheader("Results")
st.write("Your area is", area)
st.write("Your perimeter is", perimeter)

# Optional: Draw a simple rectangle
st.subheader("Visual Representation")
if length > 0 and width > 0:
    st.write("⬛" * int(length), "\n" * int(width))
else:
    st.write("Enter positive values to see the rectangle.")


