import streamlit as st

# FLAMES Calculation Logic
def calculate_flames(name1, name2):
    # Remove spaces and convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Remove common letters
    for letter in name1[:]:  # Iterate over a copy of name1
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)

    # Calculate the remaining letters count
    remaining_count = len(name1) + len(name2)

    # FLAMES Logic
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(flames) > 1:
        split_index = (remaining_count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames.pop()

    return flames[0]

# Streamlit UI
def flames_game_app():
    st.title(" FLAMES Game ")
    st.write("Find out the relationship between two names!")

    # Input Fields
    name1 = st.text_input("Enter the first name", "")
    name2 = st.text_input("Enter the second name", "")

    # Calculate FLAMES on button click
    if st.button("Find Relationship"):
        if name1 and name2:
            relationship = calculate_flames(name1, name2)
            st.success(f"The relationship between **{name1}** and **{name2}** is: **{relationship}**")
        else:
            st.warning("Please enter both names to calculate the relationship.")

if __name__ == "__main__":
    flames_game_app()
