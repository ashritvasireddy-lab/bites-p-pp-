import streamlit as st
import pandas as pd

# --- Initialize votes in session_state ---
if "Cats" not in st.session_state:
    st.session_state.Cats = 0
if "Dogs" not in st.session_state:
    st.session_state.Dogs = 0

st.title("🐱 Cats vs Dogs 🐶 Poll")
st.write("Vote for your favorite and see the results live!")

# Poll radio button
choice = st.radio("Which do you prefer?", ("Cats", "Dogs"))

# Vote button
if st.button("Vote!"):
    if choice == "Cats":
        st.session_state.Cats += 1
    else:
        st.session_state.Dogs += 1
    st.success(f"Thanks for voting for {choice}!")

# Show results as a bar chart
st.subheader("Poll Results")

votes = {"Cats": st.session_state.Cats, "Dogs": st.session_state.Dogs}
total_votes = sum(votes.values())

if total_votes == 0:
    st.write("No votes yet.")
else:
    # Convert to DataFrame for graph
    df = pd.DataFrame(list(votes.items()), columns=["Animal", "Votes"])
    st.bar_chart(df.set_index("Animal"))
    # Optional: show percentage
    for animal, count in votes.items():
        st.write(f"{animal}: {count} vote(s) ({count/total_votes*100:.1f}%)")

