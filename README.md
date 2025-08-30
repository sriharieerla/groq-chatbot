# GROQ Chatbot 🤖

A self-made AI chatbot built using the **GROQ API**, developed leveraging knowledge gained during my **Data Valley internship (completed in April 2025)**. This chatbot understands natural language queries and provides intelligent responses.

## Features

- Interactive chatbot powered by GROQ API
- Understands and responds to natural language queries
- Lightweight, fast, and easy to integrate
- Secure handling of API keys
- Self-made project showcasing AI and practical development skills

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sriharieerla/groq-chatbot
   ```
2. Navigate to the project directory: cd groq-chatbot
3. Install dependencies: pip install -r requirements.txt
4. Set up your GROQ API key securely:
   Create a .env file in the root directory: GROQ_API_KEY=your_api_key_here

Add .env to .gitignore to keep it private.
Load it in your code using python-dotenv:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

Run the chatbot: python chatbot.py
