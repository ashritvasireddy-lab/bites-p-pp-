import streamlit as st
import matplotlib.pyplot as plt
import random
import time

st.set_page_config(page_title="Flappy Bird Streamlit")

st.title("Flappy Bird (Streamlit Version)")

# --- Game variables ---
if "bird_y" not in st.session_state:
    st.session_state.bird_y = 0.5
    st.session_state.bird_velocity = 0
    st.session_state.pipes = []
    st.session_state.score = 0
    st.session_state.gravity = 0.02
    st.session_state.jump_strength = -0.04
    st.session_state.running = True

# --- Button to flap ---
if st.button("Flap"):
    st.session_state.bird_velocity = st.session_state.jump_strength

# --- Update bird position ---
st.session_state.bird_velocity += st.session_state.gravity
st.session_state.bird_y += st.session_state.bird_velocity

# --- Generate pipes ---
if len(st.session_state.pipes) == 0 or st.session_state.pipes[-1][0] < 0.7:
    gap = 0.2
    pipe_height = random.uniform(0.1, 0.6)
    st.session_state.pipes.append([1.0, pipe_height, pipe_height + gap])  # [x, top, bottom]

# --- Move pipes ---
for pipe in st.session_state.pipes:
    pipe[0] -= 0.03  # speed

# --- Collision detection ---
for pipe in st.session_state.pipes:
    if 0.1 < pipe[0] < 0.15:
        if st.session_state.bird_y < pipe[1] or st.session_state.bird_y > pipe[2]:
            st.session_state.running = False

# --- Remove passed pipes and update score ---
if st.session_state.pipes and st.session_state.pipes[0][0] < -0.1:
    st.session_state.pipes.pop(0)
    st.session_state.score += 1

# --- Check boundaries ---
if st.session_state.bird_y < 0 or st.session_state.bird_y > 1:
    st.session_state.running = False

# --- Draw game using matplotlib ---
fig, ax = plt.subplots(figsize=(4,6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Draw bird
ax.plot(0.1, st.session_state.bird_y, 'bo', markersize=15)

# Draw pipes
for pipe in st.session_state.pipes:
    ax.fill_between([pipe[0], pipe[0]+0.1], 0, pipe[1], color='green')
    ax.fill_between([pipe[0], pipe[0]+0.1], pipe[2], 1, color='green')

# Draw ground
ax.fill_between([0,1],0,0.05, color='brown')

st.pyplot(fig)

st.write(f"Score: {st.session_state.score}")

# --- Game over message ---
if not st.session_state.running:
    st.write("💥 Game Over! Refresh to restart.")
