import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def summarize_text(text):
    response = client.chat.completions.create(
        model="qwen/qwen3-32",
        messages=[
            {"role": "system", "content": "You are a text summarizer."},
            {"role": "user", "content": f"Summarize this text into bullet points:\n{text}"}
        ]
    )
    return response.choices[0].message.content

# Example usage
article = """
Artificial Intelligence (AI) is a branch of computer science that focuses on building smart machines capable of performing tasks that typically require human intelligence. These tasks include problem-solving, decision-making, language understanding, and visual recognition. AI has applications in healthcare, education, finance, and many more fields.
"""

print("Summary:\n", summarize_text(article))
