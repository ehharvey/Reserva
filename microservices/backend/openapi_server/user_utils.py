# Utils for getting user info from the request

from auth0.management import Auth0
from pymongo import MongoClient
from openapi_server.models import User

auth0: Auth0 = None

def get_user_details_prod(func):
    """Decorator to get the user from the user header"""

    def wrapper(user, db: MongoClient = None, *args, **kwargs):
        """
        Wrapper to get the user from the user header
        
        :param user: The user id
        """

        kwargs["db"] = db
        kwargs["user"] = user
        auth0_user_details: dict = auth0.users.get("auth0|643db743a891bec857308e2f")
        auth0_user_roles: list = auth0.users.list_roles("auth0|643db743a891bec857308e2f")

        # Determine role of user
        role="standard"
        if "admin" in auth0_user_roles:
            role = "admin"
        elif "staff" in auth0_user_roles:
            role = "staff"
        elif "standard" in auth0_user_roles:
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
        
        # Only supply relevant kwargs to func
        func_kwargs = kwargs.copy()
        for arg in kwargs:
            if arg not in func_params:
                func_kwargs.pop(arg)


        return func(*args, **func_kwargs)
    

    return wrapper

def get_user_details_dev(func):
    """Decorator to get the user from the user header. DEVELOPMENT ONLY"""

    def wrapper(user, db: MongoClient = None, *args, **kwargs):
        """
        Wrapper to get the user from the user header
        
        :param user: The user id
        """

        kwargs["db"] = db
        kwargs["user"] = user
        kwargs["user_details"] = User(
            id="auth0|643db743a891bec857308e2f",
            email="test@example.com",
            name="Test User",
            role="standard",
            nickname="testuser",
            picture="https://github.com/ehharvey.png"
        )

        # Determine parameters of func
        func_params = func.__code__.co_varnames
        
        # Only supply relevant kwargs to func
        func_kwargs = kwargs.copy()
        for arg in kwargs:
            if arg not in func_params:
                func_kwargs.pop(arg)


        return func(*args, **func_kwargs)
    

    return wrapper

get_user_details: callable = get_user_details_dev

def configure(domain, management_api_token):
    """
    Configure the user utils
    
    :param domain: The domain of the Auth0 account
    :param management_api_token: The management API token for the Auth0 account
    """
    global auth0
    auth0 = Auth0(domain, management_api_token)
    global get_user_details
    get_user_details = get_user_details_prod

def configure_dev():
    global get_user_details

    get_user_details = get_user_details_dev