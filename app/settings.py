# -*- coding: utf-8 -*-
"""Settings for the app."""

import os

from dotenv import load_dotenv

from app.exceptions import ConfigurationException


# Load environment variables from .env file if available
load_dotenv()

# OpenAI API settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
OPENAI_API_MODEL = "gpt-3.5-turbo"
OPENAI_API_TEMPERATURE = 0.0
OPENAI_API_MAX_TOKENS = 64


# application settings
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

# application configuration validations
if OPENAI_API_KEY in (None, "SET-ME-PLEASE"):
    raise ConfigurationException("No OpenAI API key found. Please add it to your .env file.")
