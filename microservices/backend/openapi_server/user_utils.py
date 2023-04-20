# Utils for getting user info from the request

def get_user(func):
    """Decorator to get the user from the user header"""

    def wrapper(user, *args, **kwargs):
        """
        Wrapper to get the user from the user header
        
        :param user: The user id
        """

        user = request.headers.get('X-User')
        if user is None:
            return 'User not found', 401
        return func(user, *args, **kwargs)
    

    return wrapper