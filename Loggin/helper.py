from asyncio.log import logger
import logging
from pickle import FALSE
logger=logging.getLogger(__name__)
logger.propagate=False
logger.info('hello from helper')

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  datefmt='%m/%d/%Y %H:%M:%S')

#logging.debug('this is a bug message')
#logging.info('this is an info message')
#logging.warning('this is a warning message')
#logging.error('this is an error message')
#logging.critical('this is a critical message')
