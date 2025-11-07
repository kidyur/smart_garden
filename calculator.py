
class Calculator_int():
    """
    Calculator supports:
        1) calculating arithmetic operations with them

    It raises TypeError if user tries to set float numbers

    Attributes:
        __main_num (int): private number is before the *operation
        __oper_num (int): private number is after the operation

    Methods:
        summarize()
        subtract()
        multiply()
        divide()

    (*) Operation example: __main_num + __oper_num
    """

    __main_num: int = 0
    __oper_num: int = 0

    def __init__(self, val1: int = 0, val2: int = 0):
        if (float in [type(val1), type(val2)]):
            raise(TypeError)
        self.__main_num = val1
        self.__oper_num = val2

    def get_main_num(self) -> int:
        return self.__main_num
    
    def set_main_num(self, val: int):
        if (type(val) != int):
            raise(TypeError)
        self.__main_num = val

    def get_oper_num(self) -> int:
        return self.__oper_num

    def set_oper_num(self, val: int):
        if (type(val) != int):
            raise(TypeError)
        self.__oper_num = val

    def summarize(self) -> int:
        """
        Saves sum in memory stack.
        """
        sum: int = self.__main_num + self.__oper_num
        return sum

    def subtract(self) -> int:
        """
        Saves difference in memory stack. 
        """
        diff: int = self.__main_num - self.__oper_num
        return diff

    def multiply(self) -> int:
        """
        Saves product in memory stack. 
        """
        prod: int = self.__main_num * self.__oper_num
        return prod

    def divide(self) -> int:
        """ 
        Saves quotient in memory stack.
        
        :raises: Zero Division Error, if oper_num is 0.      
        """
        if (self.__oper_num == 0):
            raise(ZeroDivisionError)
        quot: int = self.__main_num // self.__oper_num
        self.results_memory.push(quot)


calc = Calculator_int(4, 2)
print(calc.summarize())

