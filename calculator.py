
class Stack():
    __stack: list = []

    def __init__(self, st: list = []):
        self.__stack = st

    def push(self, val: any):
        self.__stack.insert(0, val)

    def get(self):
        if (len(self.__stack) == 0):
            raise (IndexError)
        return self.__stack[0]
    
    def pop(self):
        self.__stack.pop(0)
    

class Calculator_int():
    """
    Calculator supports:
        1) storing two integers in memory
        2) calculating arithmetic operations with them

    It raises TypeError if user tries to set float numbers

    Attributes:
        __main_num (int): private number is before the *operation
        __oper_num (int): private number is after the operation

    Methods:
        summarize()
        subtract()
        multiply()
        divide()

        All methods calculate their operations and save 
        results in integer memory stack (resultsMemory)

    (*) Operation example: __main_num + __oper_num
    """

    results_memory: list = Stack([])

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

    def summarize(self):
        """
        Saves sum in memory stack.
        """
        sum: int = self.__main_num + self.__oper_num
        self.results_memory.push(sum)

    def subtract(self):
        """
        Saves difference in memory stack. 
        """
        diff: int = self.__main_num - self.__oper_num
        self.results_memory.push(diff)

    def multiply(self):
        """
        Saves product in memory stack. 
        """
        prod: int = self.__main_num * self.__oper_num
        self.results_memory.push(prod)

    def divide(self):
        """ 
        Saves quotient in memory stack.
        
        :raises: Zero Division Error, if oper_num is 0.      
        """
        if (self.__oper_num == 0):
            raise(ZeroDivisionError)
        quot: int = self.__main_num // self.__oper_num
        self.results_memory.push(quot)


calc = Calculator_int(4, 2)
calc.results_memory = 1
calc.results_memory.get()

