
import streamlit as st

# --- Initialize votes in session_state ---
if "Cats" not in st.session_state:
    st.session_state.Cats = 0
if "Dogs" not in st.session_state:
    st.session_state.Dogs = 0

st.title("🐱 Cats vs Dogs 🐶")
st.write("Vote for your favorite!")

# Poll radio button
choice = st.radio("Which do you prefer?", ("Cats", "Dogs"))

# Vote button
if st.button("Vote!"):
    if choice == "Cats":
        st.session_state.Cats += 1
    else:
        st.session_state.Dogs += 1
    st.success(f"Thanks for voting for {choice}!")

# Show results
st.subheader("Poll Results")
votes = {"Cats": st.session_state.Cats, "Dogs": st.session_state.Dogs}
total_votes = votes["Cats"] + votes["Dogs"]

if total_votes == 0:
    st.write("No votes yet.")
else:
    st.write(f"Total votes: {total_votes}")
    # Bar chart
    st.bar_chart(votes)
