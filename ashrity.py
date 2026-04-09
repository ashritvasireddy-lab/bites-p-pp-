import streamlit as st
import random

st.set_page_config(page_title="🎯 Game Hub", layout="centered")

# -------------------- SESSION STATE INITIALIZATION --------------------
if "step" not in st.session_state:
    st.session_state.step = "math_quiz1"
if "math1" not in st.session_state:
    st.session_state.math1 = (random.randint(1,10), random.randint(1,10))
if "math2" not in st.session_state:
    st.session_state.math2 = (random.randint(1,10), random.randint(1,10))
if "tic_board" not in st.session_state:
    st.session_state.tic_board = [" "]*9
if "player" not in st.session_state:
    st.session_state.player = "X"
if "bot" not in st.session_state:
    st.session_state.bot = "O"
if "game_active" not in st.session_state:
    st.session_state.game_active = True
if "score" not in st.session_state:
    st.session_state.score = 0

# -------------------- UTILITY FUNCTIONS --------------------
def restart_game():
    st.session_state.step = "math_quiz1"
    st.session_state.math1 = (random.randint(1,10), random.randint(1,10))
    st.session_state.math2 = (random.randint(1,10), random.randint(1,10))
    st.session_state.tic_board = [" "]*9
    st.session_state.game_active = True
    st.experimental_rerun()

# -------------------- MATH QUIZZES --------------------
def math_quiz(n1, n2, next_step, key):
    st.markdown("## 🧮 Math Quiz")
    answer = st.number_input(f"{n1} + {n2} = ?", value=0, key=key)
    if st.button("Submit", key=f"btn_{key}"):
        if answer != n1 + n2:
            st.warning("❌ Wrong! Restarting...")
            restart_game()
        else:
            st.success("✅ Correct!")
            st.session_state.step = next_step
            st.experimental_rerun()

# -------------------- LUCK GAME --------------------
def luck_game():
    st.markdown("## 🚗 Choose the Safe Path")
    col1, col2, col3 = st.columns(3)
    for i, col in enumerate([col1, col2, col3], start=1):
        if col.button(str(i)):
            st.success("🎉 You chose a safe path!")
            st.session_state.step = "tic_tac_toe"
            st.experimental_rerun()

# -------------------- TIC TAC TOE --------------------
def check_winner(board):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def bot_move():
    empty = [i for i, val in enumerate(st.session_state.tic_board) if val==" "]
    if empty:
        move = random.choice(empty)
        st.session_state.tic_board[move] = st.session_state.bot

def draw_tic_tac_toe():
    st.markdown("## 🎮 Tic Tac Toe (You vs Bot 🤖)")
    board = st.session_state.tic_board
    for i in range(0, 9, 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            cell_index = i + j
            label = board[cell_index] if board[cell_index] != " " else " "
            if col.button(label, key=f"cell_{cell_index}"):
                if board[cell_index] == " ":
                    board[cell_index] = st.session_state.player
                    winner = check_winner(board)
                    if winner == st.session_state.player:
                        st.success("🎉 You Win!")
                        st.session_state.step = "calculator"
                        st.experimental_rerun()
                    elif " " not in board:
                        st.warning("🤖 Bot wins! Restarting...")
                        restart_game()
                    else:
                        bot_move()
                        winner = check_winner(board)
                        if winner == st.session_state.bot:
                            st.warning("🤖 Bot wins! Restarting...")
                            restart_game()
                        elif " " not in board:
                            st.warning("Draw! Restarting...")
                            restart_game()
                    st.experimental_rerun()

# -------------------- CALCULATOR --------------------
def calculator():
    st.markdown("## 🧮 Calculator Unlocked 🎉")
    choice = st.radio("Choose:", ["➕ Math", "📐 Shapes"])
    
    if choice == "➕ Math":
        a = st.number_input("First number", key="calc_a")
        op = st.selectbox("Operation", ["+", "-", "*", "/"], key="calc_op")
        b = st.number_input("Second number", key="calc_b")
        if st.button("Calculate Math"):
            if op=="+": result = a+b
            elif op=="-": result = a-b
            elif op=="*": result = a*b
            elif op=="/": result = a/b if b!=0 else "Error"
            st.success(f"Result: {result}")
    else:
        shape = st.selectbox("Shape", ["Triangle","Rectangle","Square","Circle"])
        if shape=="Triangle":
            base = st.number_input("Base", key="tri_base")
            height = st.number_input("Height", key="tri_height")
            if st.button("Calculate Triangle"):
                st.success(f"Area: {0.5*base*height}")
        elif shape=="Rectangle":
            l = st.number_input("Length", key="rec_l")
            w = st.number_input("Width", key="rec_w")
            if st.button("Calculate Rectangle"):
                st.success(f"Area: {l*w}")
        elif shape=="Square":
            s = st.number_input("Side", key="sq_s")
            if st.button("Calculate Square"):
                st.success(f"Area: {s*s}")
        elif shape=="Circle":
            r = st.number_input("Radius", key="cir_r")
            if st.button("Calculate Circle"):
                st.success(f"Area: {3.14*r*r}")

# -------------------- MAIN FLOW --------------------
def main():
    if st.session_state.step=="math_quiz1":
        n1,n2 = st.session_state.math1
        math_quiz(n1,n2,"math_quiz2","q1")
    elif st.session_state.step=="math_quiz2":
        n1,n2 = st.session_state.math2
        math_quiz(n1,n2,"luck_game","q2")
    elif st.session_state.step=="luck_game":
        luck_game()
    elif st.session_state.step=="tic_tac_toe":
        draw_tic_tac_toe()
    elif st.session_state.step=="calculator":
        calculator()

main()
