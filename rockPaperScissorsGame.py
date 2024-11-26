import random
import streamlit as st

# Title and Instructions
st.title("🎮 Rock-Paper-Scissors Game")
st.write("Choose one of **rock**, **paper**, or **scissors** and play against the computer!")

# Define choices
choices = ["rock", "paper", "scissors"]

# User Input
user_choice = st.radio("Your Choice:", choices)

# Button to play
if st.button("Play"):
    # Computer's choice
    computer_choice = random.choice(choices)
    st.write(f"🖥️ Computer chose: **{computer_choice}**")

    # Determine the winner
    if user_choice == computer_choice:
        st.info("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        st.success("🎉 YOU WON!")
    else:
        st.error("😞 YOU LOSE!")

# Footer
st.write("---")
