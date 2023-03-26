import sys
from components.app import test
from src.logger import logging
from src.exception import CustomException

test()
logging.info("message from root")
logging.error("test error")
print("log from print")

try:
    1/0
except Exception as e:
    raise CustomException(e, sys)