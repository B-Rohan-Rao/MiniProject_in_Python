class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticator_decorator(function):
    """
    Checks if the sure is logged in or not.
    :param function:
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticator_decorator
def create_blog_post(user):
    """prints the username."""
    print(f"This is {user.name}'s news blog")


new_user1 = User("Rohan")
new_user2 = User("Shiva")
new_user1.is_logged_in = True

# Printing only the user that is logged in.
create_blog_post(new_user1)
create_blog_post(new_user2)
