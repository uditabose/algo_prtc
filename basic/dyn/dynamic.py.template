from abc import ABC, abstractmethod


class Dynamic(ABC):

    @abstractmethod
    def bruteforce(self):
        pass

    @abstractmethod
    def topdown(self):
        pass

    @abstractmethod
    def bottomup(self):
        pass

    def all_result(self):
        Dynamic.__log__("By bruteforce", self.bruteforce())
        Dynamic.__log__("By topdown", self.topdown())
        Dynamic.__log__("By bottomup", self.bottomup())

    @staticmethod
    def __log__(message: str, value: object):
        print("{} : {}".format(message, value))
