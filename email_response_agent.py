import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

def generate_reply(subject, body, sender_name="Customer"):
    prompt = f"""
You are a helpful and professional email assistant for a business.

Email from {sender_name}:
Subject: {subject}
Body: {body}

Generate a polite, professional, and context-aware reply email.
"""

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
    "model": "mistralai/mistral-7b-instruct",  # ✅ VALID
    "messages": [
        {"role": "user", "content": prompt}
    ]
}


    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # 🐛 DEBUG: Show full API response
    print("DEBUG: Raw response JSON:")
    print(result)

    # ✅ Check for success or error
    if "choices" not in result:
        print("⚠️ ERROR in response:")
        print(result)
        return "Sorry, I couldn't generate a reply. Check the logs above."

    return result["choices"][0]["message"]["content"]


# Test run
if __name__ == "__main__":
    subject = "Need help with my order #12345"
    body = "Hi, I placed an order 5 days ago but haven't received it yet. Can you please check?"
    sender = "John Doe"

    reply = generate_reply(subject, body, sender)
    print("\n📩 Suggested Reply:\n")
    print(reply)
