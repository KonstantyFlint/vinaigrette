import pytest

from attack.guess_key import guess_key
from test.conftest import get_cleaned_text, random_key
from algorithm.vinaigrette import encrypt, decrypt

ALICE_IN_WONDERLANDS = get_cleaned_text("test/books/alice_in_wonderland.txt")
CHRISTMAS_CAROL = get_cleaned_text("test/books/a_christmas_carol.txt")
FRANKENSTEIN = get_cleaned_text("test/books/frankenstein.txt")


@pytest.mark.parametrize(
    "key_length",
    range(3, 50)
)
@pytest.mark.parametrize(
    "plain_text",
    (
            pytest.param(
                ALICE_IN_WONDERLANDS,
                id='alice'
            ),
            pytest.param(
                CHRISTMAS_CAROL,
                id='christmas-carol'
            ),
            pytest.param(
                FRANKENSTEIN,
                id='frankenstein'
            ),
    )
)
def test_random(key_length: int, plain_text: str):
    original_key = random_key(key_length)
    cipher = encrypt(plain_text, original_key)
    guessed_key = guess_key(cipher, 100)
    decrypted = decrypt(cipher, guessed_key)

    # guessed key might sometimes be different due to repetitions, but should be equivalent
    assert guessed_key in original_key or original_key in guessed_key

    # putting the assertion value in a variable to avoid assertion errors printing contents of entire books
    text_matches = (plain_text == decrypted)
    assert text_matches, "The decrypted message doesn't match the original."


@pytest.mark.parametrize(
    "plain_text",
    (
            pytest.param(
                ALICE_IN_WONDERLANDS,
                id='alice'
            ),
            pytest.param(
                CHRISTMAS_CAROL,
                id='christmas-carol'
            ),
            pytest.param(
                FRANKENSTEIN,
                id='frankenstein'
            ),
    )
)
def test_random_large(plain_text: str):
    original_key = random_key(1000)
    cipher = encrypt(plain_text, original_key)
    guessed_key = guess_key(cipher, 2000)
    decrypted = decrypt(cipher, guessed_key)

    # guessed key might sometimes be different due to repetitions, but should be equivalent
    assert guessed_key in original_key or original_key in guessed_key

    # putting the assertion value in a variable to avoid assertion errors printing contents of entire books
    text_matches = (plain_text == decrypted)
    assert text_matches, "The decrypted message doesn't match the original."
