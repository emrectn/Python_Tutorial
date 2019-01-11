import logging
import datetime

print('Hello Guys!')
logging.basicConfig(filename='example.log', level=logging.CRITICAL)


logging.debug('DEBUG mesaj / {}'.format(datetime.datetime.now()))
logging.info('Bilgi mesaj/ {}'.format(datetime.datetime.now()))
logging.warning('Uyari mesaj/ {}'.format(datetime.datetime.now()))

logging.critical('Uyari mesajASDASD/ {}'.format(datetime.datetime.now()))

# https://www.python.tc/python-log-tutma/
# https://medium.com/gokhanyavas/loglama-a6b5f55b1836
# https://docs.python.org/3.6/library/logging.html
# https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial