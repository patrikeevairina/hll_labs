import time


class Decorator:
    def __init__(self, func):
        self.func = func
        self.history = ""

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func(*args, **kwargs)
        self.update_history(start_time, self.func.__name__, *args)
        # print(args, *args)
        func_time = time.time() - start_time
        self.print_time(func_time)

    def update_history(self, start_time, func_name, func_args):
        arg_line = ""
        for arg in func_args:
            arg_line = arg_line + "{0}, ".format(arg)
        new_line = "<{0}>: function <{1}> called with arguments <{2}>".format(start_time, func_name, arg_line)
        self.history = self.history + new_line
        # print(new_line)

    @staticmethod
    def print_time(func_time):
        print(func_time)


class HTMLDecorator(Decorator):
    @staticmethod
    def print_time(func_time):
        html_time = "<html><body>{0}</body><html>".format(func_time)
        print(html_time)


@HTMLDecorator
def _for(nums):
    res = list()
    for i in nums:
        res.append(i*i)
    return res


@HTMLDecorator
def _lst(nums):
    return list(i*i for i in nums)


@HTMLDecorator
def _mp(nums):
    return list(map(lambda i: i*i, nums))


num_list = [i + i % 3 for i in range(1000)]
_for(num_list)
_lst(num_list)
_mp(num_list)