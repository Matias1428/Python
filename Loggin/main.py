import logging

from isort import stream
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  datefmt='%m/%d/%Y %H:%M:%S')

#import helper

logger=logging.getLogger(__name__)
#create a handler
stream_h=logging.StreamHandler()
file_h=logging.FileHandler('file.log')

#level and the format
stream_h.setLevel(logging.WARNING)
stream_h.setLevel(logging.ERROR)

formatter=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is a error')