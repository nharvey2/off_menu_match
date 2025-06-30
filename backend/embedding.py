"""File containing functions related to word/sentence embeddings"""
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
model = SentenceTransformer('all-MiniLM-L6-v2')
from config import MENU_DATA_STORE, EMBEDDINGS_INDEX

dimension = 384
index = faiss.IndexFlatL2(dimension)

def return_embedded_dictionary(menu_dict: dict[str, str], embedding_model: SentenceTransformer) -> np.ndarray:
    """Take an input dictionary and convert it to an embedding.

    Args:
        menu_dict (dict[str, str]): Dictionary to embed.
        embedding_model (SentenceTransformer): Embedding model to use.

    Returns:
        embedding (np.ndarray): Embedding for inputted menu dictionary.
    """
    dict_str = ' '.join(f"{key}: {value}" for key, value in menu_dict.items())
    embedding = embedding_model.encode(dict_str).astype('float32').reshape(1,-1)

    return embedding

def return_most_similar_menu(inputted_menu: dict) -> tuple[dict, int]:
    """Return the most similar menu to that inputted by the user by referring to the menu embeddings index and returning the
        celebrity dictionary that is closest in terms of euclidean distance.

    Args:
        inputted_menu (dict[str, str]): The dictionary of the menu inputted by the user.

    Returns:
        tuple[dict, int]: Returns a dictionary containing the closest celebrity menu and the euclidean distance.
    """
    menu_embedding = return_embedded_dictionary(inputted_menu, model)

    distance, indices = EMBEDDINGS_INDEX.search(menu_embedding, 1)

    closest_menu = MENU_DATA_STORE[indices[0][0]]

    return closest_menu, distance