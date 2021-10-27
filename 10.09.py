# NewType используется для указания проверяющему типу,
#  что некоторые значения следует рассматривать 
#  как их собственный тип
def show(func):
        def new_func(*args, **kwargs):
                print('Running function: ', func.__name__)
                print('Position arguments are: ', args)
                print('Keyword arguments are: ', kwargs)
                result = func(*args, **kwargs)
                print('Result: ' , result)
                return result
        return new_func
def decorator(function_to_decorate):
        def upgrade(new_func):
                function_to_decorate(new_func)
                return new_func
        return upgrade

def sum_(a,b):
        return a+b


cooler_sum = show(sum_)
cooler_sum(1,5)



