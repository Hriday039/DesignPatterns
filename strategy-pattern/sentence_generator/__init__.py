from typing import List, Callable


class SentenceGenerator:
    """
    A strategy class that generates and returns a random sentence.
    """

    def __init__(
        self,
        word_transform_strategy: Callable[[str], str],
        sentence_generation_strategy: Callable[[List[str]], None],
    ):
        """
        Initialize the strategy.
        """
        self.__vocab: List[str] = []
        self.__word_transform_strategy: Callable[[str], str] = word_transform_strategy
        self.__sentence_generation_strategy: Callable[
            [List[str]], None
        ] = sentence_generation_strategy

    def add_to_vocab(self) -> None:
        """
        Add a word to the vocabulary after performing transformation strategy.
        """
        word = input()
        transformed_word: str = self.__word_transform_strategy(word)
        self.__vocab.append(transformed_word)

    def print_generate_sentence(self) -> None:
        """
        Return a sentence generated with sentence generation strategy.
        """
        self.__sentence_generation_strategy(self.__vocab)
