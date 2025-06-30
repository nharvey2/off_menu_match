import streamlit as st
from pathlib import Path
import json
from backend.config import EMOJI_MAP

current_file = Path(__file__).resolve()
repo_root = current_file.parents[1]
data_path = repo_root / 'data'


st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Off Menu Match")
st.write("Input your dream menu below, and find out which celebrity you have the most similar menu with")

still_or_sparkling = st.text_input("Still or Sparkling?")
poppadoms_or_bread = st.text_input("Poppadoms or Bread?")
starter = st.text_input("Starter?")
main_course = st.text_input("Main Course?")
side_dish = st.text_input("Side Dish?")
drink = st.text_input("Drink?")
dessert = st.text_input("Dessert?")

if st.button("Submit Order"):
    order = {
        "Still or Sparkling Water": still_or_sparkling,
        "Poppadoms and/or Bread": poppadoms_or_bread,
        "Starter": starter,
        "Main Course": main_course,
        "Side Dish": side_dish,
        "Drink": drink,
        "Dessert": dessert
    }

    with open(f"{data_path}/menu_dict.json", "w") as f:
        json.dump(order, f, indent=4)

    st.subheader("Your Order Summary:")
    for key, value in order.items():
        emoji = EMOJI_MAP.get(key, "")
        st.markdown(f"- {emoji} **{key}**: {value}")
    st.markdown("Please proceed to the next page to see your results.")
