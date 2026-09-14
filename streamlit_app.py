import streamlit as st

game_page = st.Page("game.py", title="Play dessert guessing game", icon=":material/cake:")
about_page = st.Page("about.py", title="What the page is about", icon=":material/icecream:")

pg = st.navigation([game_page, about_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()