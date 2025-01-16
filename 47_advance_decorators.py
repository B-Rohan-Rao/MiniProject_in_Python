def logging_decorator(function):
    def wrapper(*args):
        # Log the function name and arguments
        print(f"You called {function.__name__}{args}")
        # Log the return value
        print(f"It returned: {function(*args)}")

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


# Call the function
a_function(1, 2, 3)
