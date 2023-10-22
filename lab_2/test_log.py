from log import Log


def test_singleton():
    log_1 = Log()
    log_2 = Log()
    assert log_1 == log_2

