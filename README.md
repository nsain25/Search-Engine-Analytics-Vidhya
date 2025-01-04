# Search-Engine-Analytics-Vidhya
The goal was to build a Smart Search System for Analytics Vidhya’s free courses, enabling users to efficiently search and discover relevant courses using natural language queries.

🛠️ Tools and Technologies Used:
- Python: Programming language for data processing and backend logic.
- BeautifulSoup & Selenium: For web scraping course data.
- Pandas: For data preprocessing and manipulation.
- HuggingFace Transformers (SentenceTransformer): For generating semantic embeddings.
- FAISS (Facebook AI Similarity Search): For efficient similarity search.
- Gradio: For building an interactive user interface.
- Google Colab: For development and deployment.

📊 Data Collection and Preprocessing:
Course data (Title, Description, Links) was scraped from Analytics Vidhya Free Courses. Preprocessing included:
- Lowercasing text.
- Removing special characters.
- Removing unnecessary whitespaces.

🤖 Embedding and Search Mechanism:
- Used all-MiniLM-L6-v2 (SentenceTransformer) to generate semantic embeddings for course titles and descriptions.
- Stored embeddings in FAISS for fast similarity searches.
- A user query is embedded and compared with the stored embeddings to return the top matching courses.

💻 Deployment and User Interface:
- A Gradio interface was built for user-friendly interaction.
- The system was deployed on Google Colab with a shareable public link.

📈 Results:
- Users can input natural language queries.
- The system returns relevant courses with titles, descriptions, and direct links.
