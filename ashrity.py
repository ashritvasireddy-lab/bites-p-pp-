import streamlit as st
import random

st.set_page_config(page_title="🎯 Game Hub", layout="centered")

# -------------------- SESSION STATE --------------------
if "step" not in st.session_state:
    st.session_state.step = "math_quiz1"
if "math1" not in st.session_state:
    st.session_state.math1 = (random.randint(1,10), random.randint(1,10))
if "math2" not in st.session_state:
    st.session_state.math2 = (random.randint(1,10), random.randint(1,10))
if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# -------------------- UTILITY --------------------
def restart_game():
    st.session_state.step = "math_quiz1"
    st.session_state.math1 = (random.randint(1,10), random.randint(1,10))
    st.session_state.math2 = (random.randint(1,10), random.randint(1,10))
    st.session_state.answer_submitted = False
    st.experimental_rerun()

# -------------------- MATH QUIZ --------------------
def math_quiz(n1, n2, next_step, key):
    st.markdown("## 🧮 Math Quiz")
    answer = st.number_input(f"{n1} + {n2} = ?", value=0, key=key)
    if st.button("Submit", key=f"btn_{key}"):
        st.session_state.answer_submitted = True
        st.session_state.answer_value = answer

    if st.session_state.answer_submitted:
        if st.session_state.answer_value != n1 + n2:
            st.warning("❌ Wrong! Restarting...")
            restart_game()
        else:
            st.success("✅ Correct!")
            st.session_state.step = next_step
            st.session_state.answer_submitted = False
            st.experimental_rerun()

# -------------------- MAIN FLOW --------------------
def main():
    if st.session_state.step=="math_quiz1":
        n1, n2 = st.session_state.math1
        math_quiz(n1, n2, "math_quiz2", "q1")
    elif st.session_state.step=="math_quiz2":
        n1, n2 = st.session_state.math2
        math_quiz(n1, n2, "next_step_placeholder", "q2")
    else:
        st.write("Next step goes here...")

main()
