# -*- coding: utf-8 -*-
"""
A simple Python example of using the OpenAI API to translate "Hello World" to a popular language.

to run in dev:
    python -m app.hello_world

to run in prod:
    CONTAINER_NAME=hello_world
    docker run -it -e OPENAI_API_KEY=${OPENAI_API_KEY} -e ENVIRONMENT=prod ${CONTAINER_NAME}
"""
import random
from typing import Optional

import openai
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from app import settings


def hello_world(language: Optional[str] = None):
    """Translate 'Hello World' to a popular language."""

    # Set the OpenAI API key
    # -------------------------------------------------------------------------
    openai.api_key = settings.OPENAI_API_KEY

    # Set the language to translate to
    # -------------------------------------------------------------------------
    if language is None:
        random_index = random.randint(0, len(settings.LANGUAGES) - 1)
        language = settings.LANGUAGES[random_index]
    languages_str = ", ".join(settings.LANGUAGES)

    # setup our text completion prompt
    # -------------------------------------------------------------------------
    prompt = f"Translate 'Hello World' to {language}"
    model = settings.OPENAI_API_MODEL
    temperature = settings.OPENAI_API_TEMPERATURE
    max_tokens = settings.OPENAI_API_MAX_TOKENS
    messages: list[ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam] = [
        ChatCompletionSystemMessageParam(
            role="system",
            content=f"""You are a helpful assistant who speaks {languages_str}
             You should respond with the correct, closest translation of "hello world" based on the language that the user
             requests. Your response should be in the format: '[hello world translation] -- ([language])'.""",
        ),
        ChatCompletionUserMessageParam(role="user", content=prompt),
    ]

    # Call the OpenAI API
    # -------------------------------------------------------------------------
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    # Print the response
    # -------------------------------------------------------------------------
    return_dict = response.model_dump()
    retval = return_dict["choices"][0]["message"]["content"]
    print(retval)
    return retval


if __name__ == "__main__":
    print("Hello World")
    input_language = input("Your language: ")
    hello_world(language=input_language)
