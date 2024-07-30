# *args acts as a tuple and **kwargs acts as a dict.
# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum_val = 0
    for n in args:
        sum_val += n
    return sum_val
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyword Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        """we can also use "kw["make"]" as it is a library but 
        it will show up an error when any attribute is not filled
        like it will show up an error if any one of the make, model, colour, seats is not filled
        and that is why we are using get function, it will assign values as None if anything is not filled"""
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
