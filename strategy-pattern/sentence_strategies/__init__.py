from typing import List
from random import shuffle


def random_sentence_strategy(vocab: List[str]) -> str:
    """
    A strategy function that generates and returns a random sentence.
    """
    return " ".join(shuffle(vocab))


def regular_sentence_strategy(vocab: List[str]) -> str:
    """
    A strategy function that generates and returns a regularly ordered sentence.
    """
    return " ".join(vocab)


def sorted_sentence_strategy(vocab: List[str]) -> str:
    """
    A strategy function that generates and returns a sorted sentence.
    """
    return " ".join(sorted(vocab))


def lowercase_transform_strategy(word: str) -> str:
    """
    A strategy function that transforms a word into lowercase word.
    """
    return word.lower()


def uppercase_reverse_transform_strategy(word: str) -> str:
    """
    A strategy function that transforms a word into reverse uppercase word.
    """
    return word[::-1].upper()
