import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API = os.getenv("GROQ_API", None)
MODEL_START = os.getenv("MODEL_START", None)