import random

ALL_CHARACTERS = [chr(i + ord('a')) for i in range(26)]


def get_cleaned_text(file_path):
    with open(file_path, encoding='utf-8') as file:
        return clean_message(file.read())


def random_key(length: int):
    return "".join(random.choice(ALL_CHARACTERS) for _ in range(length))


def clean_message(text: str) -> str:
    return "".join(
        c.lower() for c in text if c.lower() in ALL_CHARACTERS
    )
