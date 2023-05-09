from apple import apple
import logging
from logging import NullHandler

nh = NullHandler()
logging.basicConfig(
    handlers=[nh],
)

apple()

