# ########## PYTHON START ##########

import streamlit as st
import random

# ----------------- Game State -----------------
if "board" not in st.session_state:
    st.session_state.board = [" " for _ in range(9)]
if "player" not in st.session_state:
    st.session_state.player = "X"
if "bot" not in st.session_state:
    st.session_state.bot = "O"
if "score" not in st.session_state:
    st.session_state.score = 0
if "step" not in st.session_state:
    st.session_state.step = "math_quiz1"

# ----------------- Helper Functions -----------------
def reset_board():
    st.session_state.board = [" " for _ in range(9)]
    st.session_state.step = "tictactoe"

def check_winner():
    b = st.session_state.board
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b_,c in win_positions:
        if b[a] == b[b_] == b[c] and b[a] != " ":
            return b[a]
    return None

def bot_move():
    empty = [i for i, val in enumerate(st.session_state.board) if val == " "]
    if empty:
        st.session_state.board[random.choice(empty)] = st.session_state.bot

def draw_board():
    b = st.session_state.board
    st.write("## 🎮 Tic Tac Toe (You vs Bot 🤖)")
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            if st.button(b[i] if b[i] != " " else str(i+1)):
                player_move(i)

def player_move(i):
    if st.session_state.board[i] == " ":
        st.session_state.board[i] = st.session_state.player

        winner = check_winner()
        if winner == st.session_state.player:
            st.success("🎉 You Win!")
            st.session_state.step = "calculator"
            return
        if " " not in st.session_state.board:
            st.warning("🔄 It's a tie! Restarting game...")
            reset_board()
            return

        bot_move()

        winner = check_winner()
        if winner == st.session_state.bot:
            st.error("🤖 Bot Wins!")
            reset_board()
            return
        if " " not in st.session_state.board:
            st.warning("🔄 It's a tie! Restarting game...")
            reset_board()
            return

# ----------------- Game Steps -----------------
def math_quiz(n1, n2, step_next):
    ans = st.number_input(f"{n1} + {n2} = ?", value=0)
    if st.button("Submit"):
        if ans != n1 + n2:
            st.warning("❌ Wrong! Restarting...")
            st.session_state.step = "math_quiz1"
        else:
            st.success("✅ Correct!")
            st.session_state.step = step_next

def luck_game():
    st.write("## 🚗 Choose the Safe Path")
    choice = st.radio("Pick a path:", ["1","2","3"])
    if st.button("Go"):
        st.success("🎉 You chose a safe path!")
        reset_board()

def calculator():
    st.write("## 🧮 Calculator Menu")
    calc_choice = st.selectbox("Choose:", ["Math", "Shapes"])
    if calc_choice == "Math":
        a = st.number_input("Enter first number:", value=0)
        op = st.selectbox("Choose operation:", ["+", "-", "*", "/"])
        b = st.number_input("Enter second number:", value=0)
        if st.button("Calculate"):
            if op == "+": result = a + b
            elif op == "-": result = a - b
            elif op == "*": result = a * b
            elif op == "/": result = a / b if b != 0 else "Error"
            st.write(f"Result: {result}")
    else:
        shape = st.selectbox("Shape:", ["Triangle","Rectangle","Square","Circle"])
        if shape == "Triangle":
            base = st.number_input("Base:", value=0)
            height = st.number_input("Height:", value=0)
            if st.button("Calculate Area"):
                st.write(f"Area: {0.5 * base * height}")
        elif shape == "Rectangle":
            l = st.number_input("Length:", value=0)
            w = st.number_input("Width:", value=0)
            if st.button("Calculate Area"):
                st.write(f"Area: {l*w}")
        elif shape == "Square":
            s = st.number_input("Side:", value=0)
            if st.button("Calculate Area"):
                st.write(f"Area: {s*s}")
        elif shape == "Circle":
            r = st.number_input("Radius:", value=0)
            if st.button("Calculate Area"):
                st.write(f"Area: {3.14 * r * r}")

# ----------------- Main Flow -----------------
st.title("🎯 Game Hub Challenge Mode")

if st.session_state.step == "math_quiz1":
    math_quiz(random.randint(1,10), random.randint(1,10), "math_quiz2")
elif st.session_state.step == "math_quiz2":
    math_quiz(random.randint(1,10), random.randint(1,10), "luck_game")
elif st.session_state.step == "luck_game":
    luck_game()
elif st.session_state.step == "tictactoe":
    draw_board()
elif st.session_state.step == "calculator":
    calculator()

# ########## PYTHON END ##########
