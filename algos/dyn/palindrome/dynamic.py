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
        Dynamic.__log__("By bruteforce", vars(self), self.bruteforce())
        Dynamic.__log__("By topdown", vars(self), self.topdown())
        Dynamic.__log__("By bottomup", vars(self), self.bottomup())

    @staticmethod
    def __log__(message: str, original: object, result: object):
        print("{} : {} : {}".format(message, original, result))
