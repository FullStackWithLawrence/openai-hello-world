"""

run: python3 -m app.hello_world "Chinese"
"""
import argparse
import random

import openai

from app import settings


def hello_world(language: str = None):
    """Translate 'Hello World' to a popular language."""

    openai.api_key = settings.OPENAI_API_KEY
    if language is None:
        random_index = random.randint(0, len(settings.LANGUAGES) - 1)
        language = settings.LANGUAGES[random_index]
    prompt = f"Translate 'Hello World' to {language}"
    model = "gpt-3.5-turbo"
    temperature = 0.0
    max_tokens = 64
    messages = [
        {
            "role": "system",
            "content": """You are a helpful assistant who speaks English, Spanish, 
             Italian, French, Gereman, Polish, Hebrew, Chinese, Mandarin, Japanese, Hindi, Russian, 
             Portuguese, Bengali, Urdu, Indonesian, Nigerian Pidgin, Marathi, Telugu, Turkish and Tamil.
             You should respond with the correct, closest translation of "hello world" based on the language that the user
             requests. Your response should be in the format: '[hello world translation] -- ([language])'.""",
        },
        {"role": "user", "content": prompt},
    ]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return_dict = response.model_dump()

    print(return_dict["choices"][0]["message"]["content"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hello World")
    parser.add_argument(
        "--language", type=str, help="Your language", nargs="?", default=None, choices=settings.LANGUAGES
    )
    args = parser.parse_args()

    hello_world(language=args.language)
