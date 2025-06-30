import streamlit as st
from backend.embedding import return_most_similar_menu
from backend.config import EMOJI_MAP
import json

INPUTTED_MENU_PATH = "data/menu_dict.json"

st.set_page_config(page_title="Results", page_icon="🍽️")

st.title("Results")

if st.button("Click to generate results"):
    st.write("Please wait while the results are generated. This may take a few moments.")
    with open(INPUTTED_MENU_PATH, "r") as f:
        inputted_menu = json.load(f)
    most_similar_menu, distance = return_most_similar_menu(inputted_menu)
    celebrity = list(most_similar_menu.keys())[0]
    menu = most_similar_menu[celebrity]

    st.write(f"The celebrity who you have the closest dream menu with is {celebrity}")
    st.write(f"### Euclidean distance: {distance[0][0]:.2f}")
    st.write(f"### {celebrity}'s Menu")
    for key, value in menu.items():
        emoji = EMOJI_MAP.get(key, "")
        st.markdown(f"- {emoji} **{key}**: {value}")
    st.write(f"### Your Menu")
    for key, value in inputted_menu.items():
        emoji = EMOJI_MAP.get(key, "")
        st.markdown(f"- {emoji} **{key}**: {value}")



