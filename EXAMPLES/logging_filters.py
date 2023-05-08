#TODO: FINISH THIS -- currently just a copy of logging_multiple (before removing) filters
import logging
import logging.handlers
import sys
from getpass import getpass

DEBUG_LOG_FILENAME = '../LOGS/debug.log'
WARNING_LOG_FILENAME = '../LOGS/warning.log'
CRITICAL_LOG_FILENAME = '../LOGS/warning.log'

class LevelFilter(logging.Filter):
    def __init__(self, min_level, max_level):
        self._min = min_level
        self._max = max_level

    def filter(self, record):
        return self._min <= record.levelno <= self.max

# set up formatting for all handler (could be different for each)
formatter = logging.Formatter('%(levelname) %(name) %(asctime)s %(message)s')

# log to STDOUT for DEBUG only
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
stream_handler.addFilter(LevelFilter(logging.DEBUG, logging.DEBUG))

# log to a file for all levels WARNING and higher
file_handler = logging.FileHandler(WARNING_LOG_FILENAME)
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

SMTP_PASSWORD = getpass("smtp password: ")

# log to email for CRITICAL
email_handler = logging.handlers.SMTPHandler(
    ('smtp2go.com', 2525),
    'TestLogger@pythonclass.com',
    ['jstrick@mindspring.com'],
    'ThisApplication Log Entry',
    ('pythonclass', SMTP_PASSWORD),
)
email_handler.setLevel(logging.CRITICAL)



testlogger = logging.getLogger('TestLogger')  # create Logger object

testlogger.addHandler(stream_handler)
testlogger.addHandler(file_handler)
testlogger.addHandler(email_handler)

testlogger.setLevel(logging.DEBUG)  # optional

# create shortcut functions for levels
debug = testlogger.debug
info = testlogger.info
warning = testlogger.warning
error = testlogger.error
critical = testlogger.critical
