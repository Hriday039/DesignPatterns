from typing import List, Callable


class SentenceGenerator:
    """
    A strategy class that generates and returns a random sentence.
    """

    def __init__(
        self,
        word_transform_strategy: Callable[[str], str],
        sentence_generation_strategy: Callable[[List[str]], str],
    ):
        """
        Initialize the strategy.
        """
        self.__vocab: List[str] = []
        self.__word_transform_strategy = word_transform_strategy
        self.__sentence_generation_strategy = sentence_generation_strategy

    def add_to_vocab(self, word: str) -> None:
        """
        Add a word to the vocabulary after performing transformation strategy.
        """
        transformed_word: str = self.__word_transform_strategy(word)
        self.__vocab.append(transformed_word)

    def generate_sentence(self) -> str:
        """
        Return a sentence generated with sentence generation strategy.
        """
        return self.__sentence_generation_strategy(self.__vocab)
