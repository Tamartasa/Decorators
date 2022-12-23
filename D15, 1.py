#Implement a decorator @single_str_arg that validates that function received
# exactly one argument and that the argument type is string. If the validation fails,
# the decorator should raise an InvalidArgument exception.

class InvalidArgument(Exception):
    pass

def single_str_arg(other_func):
    def decorated_func(*arg, **kwargs):
        if len(arg) != 1 or len(kwargs) != 0 or not isinstance(arg[0], str):
            raise InvalidArgument("argument must be exactly one and a string")
        return other_func(*arg, **kwargs)
    return decorated_func

@single_str_arg
def check_str(word: str):
    print(word)

if __name__ == '__main__':

    check_str('tamar')
    check_str('tamar', 'gal')
    check_str(9)
