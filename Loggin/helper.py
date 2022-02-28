import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  cldatefmt='%m/%d/%Y %H:%M:%S')

logging.debug('this is a bug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')
