# Off Menu Match

Ever wondered whose *Off Menu* menu is most similar to yours? Well now you can find out!

Simply enter your menu preferences, and the app matches you to the closest celebrity menu from past guests on the show.

This tool uses text embeddings to compare your menu to that of its *Off Menu* menu database, and returns the menu that is closest to yours in terms of Euclidean distance.

## Work in Progress

This tool is currently a work in progress, and is mainly for the purposes of playing around and becoming more familiar with working with text embeddings. Feedback and suggestions are very welcome!

## Features

- Compare your dream menu to celebrities from the *Off Menu* podcast
- Interactive and easy-to-use interface powered by Streamlit
- Uses similarity matching to find your best celebrity menu match

## How to Run

1. Clone the repo  
2. Install requirements (`pip install -r requirements.txt`)  
3. Run the app:  
   ```bash
   streamlit run frontend/Home.py
