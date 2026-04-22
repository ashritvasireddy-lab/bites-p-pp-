import streamlit as st

# Save value in memory
if "value" not in st.session_state:
    st.session_state.value = ""

def press(num):
    st.session_state.value += str(num)

def clear():
    st.session_state.value = ""

def calculate():
    try:
        st.session_state.value = str(eval(st.session_state.value))
    except:
        st.session_state.value = "Error"

st.title("Button Calculator")

st.text_input("Result", value=st.session_state.value, key="display")

# Buttons
cols = st.columns(4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

for i, btn in enumerate(buttons):
    if cols[i % 4].button(btn):
        if btn == "=":
            calculate()
        else:
            press(btn)

if st.button("Clear"):
    clear()
