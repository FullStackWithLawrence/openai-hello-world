# -*- coding: utf-8 -*-
"""Settings for the app."""

import os

from dotenv import load_dotenv

from app.exceptions import ConfigurationException


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)


if OPENAI_API_KEY in (None, "PLEASE-ADD-ME"):
    raise ConfigurationException("No OpenAI API key found. Please add it to your .env file.")

LANGUAGES = [
    "English",
    "Spanish",
    "Italian",
    "French",
    "Gereman",
    "Polish",
    "Hebrew",
    "Chinese",
    "Mandarin",
    "Japanese",
    "Hindi",
    "Russian",
    "Portuguese",
    "Bengali",
    "Urdu",
    "Indonesian",
    "Nigerian Pidgin",
    "Marathi",
    "Telugu",
    "Turkish",
    "Tamil",
]
