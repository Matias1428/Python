# Errors and Exceptions
from email import message
from warnings import catch_warnings


#x=-5
#assert(x>=0), 'x is no positive'

try:
    a=5/0
except:
    print('error happed')


try:
    a=7/0
except Exception as e:
    print(e)

try:
    a=7/0
    b=a+'10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:  # alwasy run
    print('Cleaning up...')


class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def test_value(x):
    if x>100:
        raise ValueTooHighError('Values is too high')
    if x<5:
        raise ValueTooSmallError('values is too small', x)
try:
    test_value(1)    
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)