import time
import abc
import types


class BaseDecorator(abc.ABC):
    def __init__(self, func):
        self._func = func
        # func_ptr = func
        # while not isinstance(func_ptr, types.FunctionType):
        #     func_ptr = func_ptr.__func
        self.__name__ = self._func.__name__
        self.history = ""  # поле, в котором хранится история
        self.time = 0

    def update_history(self, start_time, func_name, func_args):
        arg_line = ""
        for arg in func_args:
            arg_line = arg_line + "{0}, ".format(arg)
        new_line = "<{0}>: function <{1}> called with arguments <{2}>".format(start_time, func_name, arg_line)
        self.history = self.history + new_line

    # def __call__(self, *args, **kwargs):
    #     self.__func(*args, **kwargs)
    #     self.time = time.time()
    #     self.update_history(self.time, self.f_name, *args)
    #     # self.print_time()


class Decorator(BaseDecorator):
    def __init__(self, func):
        super().__init__(func)

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self._func(*args, **kwargs)
        time_delta = time.time() - start_time
        self.update_history(start_time, self._func.__name__, *args)
        print(self.history)
        return time_delta


class HTMLDecorator(BaseDecorator):

    def __call__(self, *args, **kwargs):
        time_delta = self._func(*args, **kwargs)
        self.update_history(time.time() - time_delta, self.__name__, *args)
        print(self.history)
        
    def print_time(self):
        html_time = "<html><body>{0}</body><html>".format(self.time)
        print(html_time)


# @HTMLDecorator
def _for(nums):
    res = list()
    for i in nums:
        res.append(i*i)
    return res


@HTMLDecorator
@Decorator
def _lst(nums):
    return list(i*i for i in nums)


# @HTMLDecorator
def _mp(nums):
    return list(map(lambda i: i*i, nums))


num_list = [i + i % 3 for i in range(1000)]
# _for(num_list)
_lst(num_list)
# _mp(num_list)
