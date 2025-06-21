import os
from dotenv import load_dotenv
import openai

# Load env variables (Railway handles this automatically, but safe to include)
load_dotenv()

# Load OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test the connection
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have confirmed access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Who are you?"}
        ]
    )
    print("[SUCCESS] GPT Response:")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"[ERROR] {e}")
