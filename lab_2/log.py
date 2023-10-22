import os
import time


class Log:
    _instance = None
    _filename = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        cls._filename = os.path.join(os.getcwd(), "log.txt")
        f = open(cls._filename, 'w')
        f.close()
        return cls._instance

    def debug(self, message):
        with open(self._filename, 'a') as f:
            f.write("[DEBUG]<{0}>:{1}\n".format(time.time(), message))

    def info(self, message):
        with open(self._filename, 'a') as f:
            f.write("[INFO]<{0}>:{1}\n".format(time.time(), message))

    def warn(self, message):
        with open(self._filename, 'a') as f:
            f.write("[WARN]<{0}>:{1}\n".format(time.time(), message))

    def error(self, message):
        with open(self._filename, 'a') as f:
            f.write("[ERROR]<{0}>:{1}\n".format(time.time(), message))

    def critical(self, message):
        with open(self._filename, 'a') as f:
            f.write("[CRITICAL]<{0}>:{1}\n".format(time.time(), message))


def test_code():
    log = Log()
    log.info("[test_code] start")
    rand_state = int(time.time()) % 2
    # rand_state = 0
    if rand_state == 1:
        l = list(i % 7 for i in range(100))
    else:
        l = list()
    log.debug("list len = {0}".format(len(l))) if len(l) > 0 else log.warn("empty list")
    try:
        l.pop()
    except Exception:
        log.error("pop from this list is not available")
    log.info("[test_code] end")


test_code()
