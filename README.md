# Off Menu Match

Ever wondered whose *Off Menu* menu is most similar to yours? Well now you can find out!

Simply enter your menu preferences, and the app matches you to the closest celebrity menu from past guests on the show.

This tool uses text embeddings to compare your menu to that of its *Off Menu* menu database, and returns the menu that is closest to yours in terms of Euclidean distance.

## Work in Progress

This tool is currently a work in progress, and is mainly for the purposes of playing around and becoming more familiar with working with text embeddings. Feedback and suggestions are very welcome!

## Data Gathering

To gather the data, I first started by scraping the *Off Menu* website for any links that contained the word "Transcript", as these would most likely be transcripts from podcast episodes. Once I had a list of links to the PDFs containing the transcripts, I downloaded each PDF.

Using PdfReader, I extracted the text from the last 10 pages of the transcript - as this is typically where the final menu will be read out. I then used a Google Gemini model (gemini-2.0-flash) and instructed it to extract the menus from the provided text. These are then stored in a json dictionary, which can be seen in the file menus_data_store.json. After this, I converted each celebrity menu into embeddings using SentenceTransformer and stored them in a FAISS index - ready to be compared with whatever the user inputs as their ideal menu.

## How to Run

1. Clone the repo  
2. Install requirements (`pip install -r requirements.txt`)  
3. Run the app:  
   ```bash
   streamlit run frontend/Home.py
