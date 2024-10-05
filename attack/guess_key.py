from collections import deque
from itertools import cycle
from math import dist

from attack.guess_key_length import guess_key_length

LETTER_FREQUENCIES = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
# ENGLISH FREQUENCIES


def get_frequencies_for_parts(cipher: str, key_length: int) -> tuple[deque[float]]:
    buckets = [[0 for _ in range(26)] for _ in range(key_length)]
    for bucket_number, letter in zip(cycle(range(key_length)), cipher):
        buckets[bucket_number][ord(letter) - ord('a')] += 1

    result = []
    for bucket in buckets:
        bucket_sum = sum(bucket)
        result.append(deque(count / bucket_sum for count in bucket))
    return tuple(result)


def get_best_offset(frequencies: deque[float]) -> int:
    best_offset = 0
    best_distance = float("inf")
    for offset in range(26):
        distance = dist(frequencies, LETTER_FREQUENCIES)
        if distance < best_distance:
            best_distance = distance
            best_offset = offset
        frequencies.append(frequencies.popleft())
    return best_offset


def guess_key(cipher: str, max_key_length: int) -> str:
    key_length = guess_key_length(cipher, max_key_length)
    buckets = get_frequencies_for_parts(cipher, key_length)
    return "".join(chr(get_best_offset(bucket) + ord('a')) for bucket in buckets)
