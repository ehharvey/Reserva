# Utils for getting user info from the request

from auth0.management import Auth0
from openapi_server.models import User

auth0: Auth0 = None

def get_user_details(func):
    """Decorator to get the user from the user header"""

    def wrapper(user, *args, **kwargs):
        """
        Wrapper to get the user from the user header
        
        :param user: The user id
        """
        
        kwargs["user"] = user
        auth0_user_details: dict = auth0.users.get("auth0|643db743a891bec857308e2f")

        # Determine role of user
        # TODO: Change this to pull from the database
        role = "standard"

        # Determine parameters for User object constructor
        user_params = User.__init__.__code__.co_varnames

        # Pop out parameters that are not in the User object
        for param in list(auth0_user_details.keys()):
            if param not in user_params:
                auth0_user_details.pop(param)

        # Create User object from auth0 user details
        kwargs["user_details"] = User(
            **auth0_user_details,
            role=role
        )

        if user is None:
            return 'User not found', 401
        
        # Determine parameters of func
        func_params = func.__code__.co_varnames
        
        # Only supply user, user_details, and/or token_info if they are
        # parameters of the decorated function
        if "user" not in func_params:
            kwargs.pop("user", None)
        if "user_details" not in func_params:
            kwargs.pop("user_details", None)
        if "token_info" not in func_params:
            kwargs.pop("token_info", None)

        return func(*args, **kwargs)
    

    return wrapper

def configure(domain, management_api_token):
    """
    Configure the user utils
    
    :param domain: The domain of the Auth0 account
    :param management_api_token: The management API token for the Auth0 account
    """
    global auth0
    auth0 = Auth0(domain, management_api_token)