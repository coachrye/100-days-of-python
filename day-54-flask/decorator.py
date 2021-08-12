import time

# first_class objects -- passed as arguments
# nested functions
# returning functions


# Python Decorator
# A function that wraps another function... modifies it's functionality
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")
# decorated_function = delay_decorator(say_hello)
# decorated_function()

@delay_decorator
def say_bye():
    print("Bye")
# Same as
# decorated_function = delay_decorator(say_bye)
# decorated_function()


@delay_decorator
def say_greeting():
    print("greeting")

say_hello()
