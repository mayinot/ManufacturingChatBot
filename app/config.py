# utils/config.py

import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL = "gpt-4o-mini"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mes.db")
