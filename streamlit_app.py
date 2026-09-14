import streamlit as st
import random

def restart_the_game():
    # reset the state
    for key in st.session_state.keys():
        del st.session_state[key]
    st.session_state.answer_for_session = random.choice(answers)

st.title("Food Name Guesser")

answers = [
{
    "name": "Knafeh",
    "description": "a traditional Arab dessert made with kadayif layered with cheese and soaked in a sweet, sugar-based syrup called attar.",
    "image": "./statics/Künefe.jpg"
},
{
    "name": "Halo-halo",
    "description": "a popular cold dessert in the Philippines made with crushed ice, evaporated milk or sometimes coconut milk, and flavoring such as ube jam (ube halaya), sweetened kidney beans or garbanzo beans, coconut strips, sago, gulaman (agar), pinipig, boiled taro or soft yams in cubes, flan, slices or portions of fruit preserves, and other root crop preserves.",
    "image": "./statics/Halo-Halo.jpg"
},
{
    "name": "Mochi",
    "description": "a Japanese rice cake made of mochigome (もち米), a short-grain japonica glutinous rice, and sometimes other ingredients such as water, sugar, and cornstarch.",
    "image": "./statics/Rice_Cake.jpg"
}
]


max_guess = 3
# Initialize chat history
if "guesses" not in st.session_state:
    st.session_state.guesses = []
    st.session_state.guess_left = 3
    st.session_state.answer_for_session = random.choice(answers)

st.markdown(f"What is this food?")
st.image(image=st.session_state.answer_for_session["image"], width=500)

# Display chat messages from history on app rerun
for guess in st.session_state.guesses:
    with st.chat_message(guess["role"]):
        st.markdown(guess["content"])


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.guesses.append({"role": "user", "content": prompt})
    st.session_state.guess_left = max_guess - len(st.session_state.guesses)

    if st.session_state.guess_left <= 1:
        st.markdown(f"Hint: {st.session_state.answer_for_session["description"]}")

    if prompt == st.session_state.answer_for_session["name"]:
        st.write("You guessed right!!")
        st.button(label="Play again?", on_click=restart_the_game)

    elif st.session_state.guess_left == 0:
        st.write(f"Boo! It was {st.session_state.answer_for_session["name"]}")
        st.button(label="Play again?", on_click=restart_the_game)

st.markdown(f"Guesses Left: {st.session_state.guess_left}")
        


