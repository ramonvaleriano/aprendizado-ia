from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API = os.getenv("GROQ_API", "None")