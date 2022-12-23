class InvalidArgument(Exception):
    pass

def numeric_params(valid_params: list):
    def inner(func):
        def decorated(*arg, **kwargs):
            for a in arg:
                if type(a) not in valid_params:
                    raise InvalidArgument()
            for k in kwargs.values():
                if type(k) not in valid_params:
                    raise InvalidArgument()
            return func(*arg, **kwargs)
        return decorated
    return inner


@numeric_params([int, float])
def get_sum(num1, num2):
    return num1 + num2



if __name__ == '__main__':
    print(get_sum(3, 4))
    print(get_sum(3.666, 8.9))
