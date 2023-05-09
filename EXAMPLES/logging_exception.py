
import logging

logging.basicConfig( # configure logging (for 'root' logger)
    filename='../LOGS/exception.log',
    level=logging.WARNING,  # minimum level
    format=f"%(levelname)s %(pathname)s %(lineno)d %(message)s",
)

root = logging.getLogger()

def spam():
    ham = logging.getLogger('barbecue')  # no params gets root logger
    ham.warning("your hair is on fire")
    logging.error("you are on fire")
    root.debug("what is going on here?")

spam()

for i in range(3):
    try:
        result = i/0
    except ZeroDivisionError:
        root.exception('Logging with exception info') # add exception info to the log
