from typing import Optional

from sentence_generator import SentenceGenerator
from sentence_strategies import (
    random_sentence_strategy,
    regular_sentence_strategy,
    sorted_sentence_strategy,
    lowercase_transform_strategy,
    uppercase_reverse_transform_strategy,
)

rsg = SentenceGenerator(lowercase_transform_strategy, random_sentence_strategy)
ssg = SentenceGenerator(lowercase_transform_strategy, sorted_sentence_strategy)
osg = SentenceGenerator(uppercase_reverse_transform_strategy, regular_sentence_strategy)


def getMenuChoice() -> Optional[int]:
    options = [
        "add word to rsg vocab",
        "add word to ssg vocab",
        "add word to osg vocab",
        "execute rsg",
        "execute ssg",
        "execute osg",
    ]

    for i, option in enumerate(options):
        print(i + 1, option)

    print(" -> Choose from the options above")
    print(" -> Press Ctrl-C to terminate the program")

    try:
        choice = int(input().strip())
        return choice
    except ValueError:
        print("Invalid choice")
        return None


functions = [
    rsg.add_to_vocab,
    ssg.add_to_vocab,
    osg.add_to_vocab,
    rsg.print_generate_sentence,
    ssg.print_generate_sentence,
    osg.print_generate_sentence,
]

if __name__ == "__main__":
    while True:
        try:
            choice: Optional[int] = getMenuChoice()
            if choice is None:
                continue
            functions[choice - 1]()

        except KeyboardInterrupt:
            print("\nTerminating program")
            break
