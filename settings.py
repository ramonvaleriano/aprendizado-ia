import os
from dotenv import load_dotenv

load_dotenv()

groq_apy_key = os.getenv("GROQ_API", None)
model_start = os.getenv("MODEL_START", None)