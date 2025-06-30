"""Config file for the off menu match app."""
import json
import faiss

EMOJI_MAP = {
    "Still or Sparkling Water": "💧",
    "Poppadoms and/or Bread": "🍞",
    "Starter": "🥗",
    "Main Course": "🍛",
    "Side Dish": "🍚",
    "Drink": "🥤",
    "Dessert": "🍨"
}

with open("menus_data_store.json", "r") as f:
    MENU_DATA_STORE = json.load(f)

EMBEDDINGS_INDEX = faiss.read_index("menu_embeddings.index")