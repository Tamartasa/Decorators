#Implement a decorator @numeric_in_range that receives as parameters allowed range
# for numeric arguments (2 numbers - min and max) and validates that all the
# numerical arguments passed to the decorated function are in the range specified.
# If the validation fails, your decorator should raise an InvalidArgument exception.
class InvalidArgument(Exception):
    pass

def numeric_in_range(min_n: int, max_n: int):
    def inner(func):
        def decorated(*args, **kwargs):
            for a in args:
                if a not in range(min_n, max_n):
                    raise InvalidArgument()
            for v in kwargs.values():
                if v not in range(min_n, max_n):
                    raise InvalidArgument()
            return func(*args, **kwargs)
        return decorated
    return inner

@numeric_in_range(1, 10)
def sum_nums(num1, num2):
    return num1 + num2

# sum_nums = numeric_in_range(1, 10)(sum_nums)(3, 5)

if __name__ == '__main__':
    try:
        print(sum_nums(3, 5))
        print(sum_nums(3, 66))
    except InvalidArgument:
        print("one or more parameter not in range")
