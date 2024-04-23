# GenAI-Data Science Tutor

This project implements an AI Data Science Tutor using Streamlit and Google's GenerativeAI API. The AI tutor, named ROBO-DSTutor, assists users in understanding data science topics by providing relevant explanations. If the user's query is not related to data science, the AI politely informs them that it cannot provide assistance.

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies by running:
    ```
    pip install streamlit google.generativeai
    ```
3. Ensure you have obtained an API key from Google's GenerativeAI API and replace `'YOUR_API_KEY'` in the code with your actual API key.

## Usage
1. Run the Streamlit app by executing the following command in your terminal:
    ```
    streamlit run AI_tutor.py
    ```
2. Once the app is running, you'll see the interface titled "AI Data Science Tutor".
3. Enter your query or data science topic in the chat input box and press Enter.
4. The AI tutor will respond with an explanation or let you know if it cannot assist with the given query.

## Files
- `AI_tutor.py`: The main Python script implementing the Streamlit app.

## Dependencies
- Streamlit: A Python library for building interactive web applications.
- Google's GenerativeAI API: Provides access to powerful AI models for generating natural language content.
