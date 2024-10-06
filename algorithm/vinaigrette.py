from itertools import cycle
from typing import Iterable


def str_to_ints(text: str, ) -> list[int]:
    return [ord(c) - ord('a') for c in text]


def ints_to_str(ints: Iterable[int]) -> str:
    return "".join(chr(num + ord('a')) for num in ints)


def encrypt(plaintext: str, key: str) -> str:
    plaintext_ints = str_to_ints(plaintext)
    key_ints = str_to_ints(key)
    return ints_to_str((base + offset) % 26 for base, offset in zip(plaintext_ints, cycle(key_ints)))


def decrypt(cipher: str, key: str) -> str:
    cipher_ints = str_to_ints(cipher)
    key_ints = str_to_ints(key)
    return ints_to_str((base - offset + 26) % 26 for base, offset in zip(cipher_ints, cycle(key_ints)))
