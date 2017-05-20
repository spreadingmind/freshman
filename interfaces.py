

from abc import ABCMeta, abstractmethod
class AbstractCalculator(object, metaclass=ABCMeta):
    @abstractmethod
    def plus(self,n,m):
        pass
    @abstractmethod
    def minus (self,n,m):
        pass
#signature = name + return type + n of parametrs + tupes of parameters


class SmartCalculator(AbstractCalculator):
    def plus(self,n,m):
        return n + m

    def minus(self,n,m):
        return n - m

class StupidCalculator(AbstractCalculator):
    def plus(self,n,m):
        return 'meh'

    def minus(self,n,m):
        return 'beh'


class CashBox:

    def __init__(self, calculator):
        self.calculator = calculator

    def evaluate_taxes(self, a, b, c, d):
        hh = self.calculator.plus(a,b)
        gg = self.calculator.plus(c,d)
        return self.calculator.minus(hh, gg)




if __name__ == "__main__":
    my_cashbox = CashBox(StupidCalculator())
