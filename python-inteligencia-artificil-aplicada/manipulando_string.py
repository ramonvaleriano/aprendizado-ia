"""
    Aprendendo a conectar a IA do google cm Python
"""
from setting_ia import GEMINI_API_KEY
from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Que tipo de IA é você?"
)

print(response.text)