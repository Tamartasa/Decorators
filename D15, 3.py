# Implement a decorator @valid_param_types that receives as parameter
# allowed argument types and validates whether the argument passed to a
# function answers this requirement. If the validation fails, the decorator
# should raise an InvalidArgument exception.
class InvalidArgument(Exception):
    pass

def valid_param_types(allowed_argument_types: list):
    def inner(func):
        def decorated_func(*arg, **kwargs):
            for a in arg:
                if type(a) not in allowed_argument_types:
                    raise InvalidArgument()
            for k in kwargs.values():
                if type(k) not in allowed_argument_types:
                    raise InvalidArgument()
            return func(*arg, **kwargs)
        return decorated_func
    return inner


@valid_param_types([int, float])
def get_sum(num1, num2):
    return num1 + num2

# get_sum = valid_param_types([int, float])(get_sum)(4, 5)


# @valid_param_types([str])
# def my_print(str1, str2):
#     print(str1, str2)

if __name__ == '__main__':
    print(get_sum(4, 5))
    # my_print('ttt', 'bbb')