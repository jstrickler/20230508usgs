"""
Demonstration of complete logging configuration.
"""
import random
import logging
from randomwords import RandomWords

LEVELS = "debug info warning error critical".split()

def main():
    """
    Program entry point.

    :return: None
    """
    random_word = RandomWords()

    my_logger = logging.getLogger(__name__)

    logging.basicConfig(
        filename='../LOGS/montylogger.log',
        level=logging.INFO,
        format="%(name)s %(levelname)s %(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    my_logger.setLevel(logging.INFO)

    levels = [getattr(my_logger, level) for level in LEVELS]

    for _ in range(100):
        logger = random.choice(levels)
        word_1 = random_word()
        word_2 = random_word()
        word_3 = random_word()
        logger('{} {} {}'.format(word_1, word_2, word_3))


if __name__ == '__main__':
    main()
