
import gradio as gr
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import re

# Load SentenceTransformer Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS Index
index = faiss.read_index('courses_index.faiss')

# Load Course Data
import pandas as pd
df = pd.read_csv('cleaned_courses.csv')

# Text Preprocessing
def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

def search_courses(query, top_k=5):
    query_embedding = model.encode([preprocess(query)])
    distances, indices = index.search(np.array(query_embedding).astype('float32'), top_k)

    results = []
    for idx in indices[0]:
        if idx < len(df):
            results.append({
                'Course Title': df.iloc[idx]['Course Title'],
                'Description': df.iloc[idx]['Description'],
            })
    return results

def search_interface(query):
    results = search_courses(query)
    if not results:
        return "No relevant courses found. Try another keyword."
    
    formatted_results = "\n\n".join(
        [f"**{res['Course Title']}**\n{res['Description']}\n[Link]({res.get('Link', '#')})" for res in results]
    )
    return formatted_results

# Launch Gradio Interface
iface = gr.Interface(
    fn=search_interface,
    inputs="text",
    outputs="markdown",
    title="Smart Course Search",
    description="Enter a query to find relevant free courses on Analytics Vidhya."
)

iface.launch()
    