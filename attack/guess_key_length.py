from collections import deque
from statistics import mean


def get_coincidence_counts(cipher: str, max_key_length: int):
    base = list(cipher)
    shifted = deque(base)
    counts = []
    for offset in range(1, max_key_length + 1):
        shifted.append(shifted.popleft())
        count = sum(1 if a == b else 0 for a, b in zip(base, shifted))
        counts.append(count)
    return counts


def guess_key_length(cipher: str, max_key_length: int) -> int | None:
    counts = get_coincidence_counts(cipher, max_key_length)
    treshold = (mean(counts) + max(counts)) / 2
    for offset, value in enumerate(counts, start=1):
        if value >= treshold:
            return offset
    return None
