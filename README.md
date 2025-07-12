# 🤖 AI Content Creator

## Overview

The AI Content Creator is a web application built with LangChain and Streamlit that leverages Large Language Models (LLMs) to generate high-quality written content. Users can choose to create full-length blog posts or catchy YouTube video titles on any given topic.

This project serves as a practical demonstration of fundamental LangChain concepts, including:
- Prompt Engineering and `PromptTemplate`
- Creating and managing `LLMChain`s
- Using `OutputParsers` for structured data extraction
- Building interactive user interfaces for AI applications with Streamlit.

<!-- TODO: Add a screenshot of the running application! -->
<!-- ![App Screenshot](https://path-to-your-image.com/screenshot.png) -->

---

## Features

- **Blog Post Generation:** Creates a well-structured, 500+ word blog post in Markdown format.
- **YouTube Title Generation:** Generates a list of 5 SEO-friendly and engaging titles for a YouTube video.
- **Interactive UI:** A simple and intuitive web interface built with Streamlit.

---

## Tech Stack

- **Framework:** LangChain
- **LLM Provider:** Groq (using the Llama 3 model)
- **UI:** Streamlit
- **Embeddings (for future projects):** Hugging Face
- **Core Libraries:** `langchain-groq`, `python-dotenv`

---

## Local Setup and Installation

To run this project locally, follow these steps:

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/ai-content-creator.git
cd ai-content-creator
```
*(Replace `your-username` with your actual GitHub username)*

**2. Create and activate a virtual environment:**
```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**3. Install dependencies:**
The `requirements.txt` file contains all the necessary Python packages.
```bash
pip install -r requirements.txt
```

**4. Set up environment variables:**
   - Create a file named `.env` in the root directory.
   - Add your Groq API key to this file:
     ```
     GROQ_API_KEY="your_api_key_here"
     ```
   - You can get a free API key from [GroqCloud](https://console.groq.com/).

**5. Run the application:**
```bash
streamlit run app.py
```
The application will now be running and accessible in your web browser at `http://localhost:8501`.

---

## Project Structure

```
.
├── .env                # Stores secret API keys (not committed to Git)
├── .gitignore          # Specifies files and folders to be ignored by Git
├── app.py              # The main Streamlit application UI and entry point
├── chain.py            # Contains the LangChain chain logic for content generation
├── README.md           # This documentation file
└── requirements.txt    # Lists the project's Python dependencies
```