import os
import time


class Log(object):
    _instance = None
    _filed = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        _filename = os.path.join(os.getcwd(), "log.txt")
        cls._filed = open(_filename, 'w')
        return cls._instance

    def __del__(self):
        self._filed.close()

    @staticmethod
    def form_str(tp, tm, msg):
        return "[{0}]<{1}>:{2}\n".format(tp, tm, msg)

    def debug(self, message):
        self._filed.write(self.form_str("DEBUG", time.time(), message))

    def info(self, message):
        self._filed.write(self.form_str("INFO", time.time(), message))

    def warn(self, message):
        self._filed.write(self.form_str("WARN", time.time(), message))

    def error(self, message):
        self._filed.write(self.form_str("ERROR", time.time(), message))

    def critical(self, message):
        self._filed.write(self.form_str("CRITICAL", time.time(), message))


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
