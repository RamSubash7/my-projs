import random
import streamlit as st

# List of characters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '*', '&', '(', ')', '>', '<', '?']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Streamlit UI components
st.title("Welcome to Password Generator")

# User inputs
n_letters = st.slider("How many letters do you want in your password?", 1, 20, 12)
n_symbols = st.slider("How many symbols do you want in your password?", 0, 10, 4)
n_numbers = st.slider("How many numbers do you want in your password?", 0, 10, 3)

# Password generation logic
password1 = ''.join(random.choice(letters) for _ in range(n_letters))
password2 = ''.join(random.choice(symbols) for _ in range(n_symbols))
password3 = ''.join(random.choice(numbers) for _ in range(n_numbers))

# Combine all parts of the password
password = password1 + password2 + password3

# Shuffle the password
x = list(password)
random.shuffle(x)
final_password = ''.join(x)

# Display the final password
st.write("Your generated password is:")
st.text(final_password)
