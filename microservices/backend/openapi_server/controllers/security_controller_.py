from typing import Callable, List
from jwt import PyJWKClient
import jwt

jwks_client: PyJWKClient = None
get_token_info: Callable[[str], dict] = None

def configure_jwk_client(domain: str):
    global jwks_client
    global get_token_info
    
    jwks_client = PyJWKClient(f"https://{domain}/.well-known/jwks.json")
    get_token_info = get_token_info_prod

def configure_jwk_client_dev():
    global jwks_client
    global get_token_info
    
    jwks_client = None
    get_token_info = get_token_info_dev

def get_token_info_prod(token: str):
    """
    Validate and decode token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    'scope' or 'scopes' will be passed to scope validation function.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    global jwks_client
    if jwks_client is None:
        raise Exception("JWK client not configured")

    signing_key = jwks_client.get_signing_key_from_jwt(token)

    claims = jwt.decode(
        token,
        signing_key.key,
        algorithms=["RS256"],
        # issuer="https://DOMAIN.com", # TODO: figure out how to verify issuer
        audience="http://localhost:8080"
        )
    
    # Get user id from token
    if 'sub' in claims:
        claims['uid'] = claims['sub']
    elif 'uid' not in claims:
        raise Exception("Token does not contain user id")

    # Get scopes from token
    if 'scope' in claims:
        claims['scopes'] = claims['scope'].split(' ')
    elif 'scopes' not in claims:
        raise Exception("Token does not contain scopes")

    return claims

ALL_SCOPES = [
    'write:groups:me',
    'read:unavailabilities:me',
    'write:unavailabilities:me',
    'write:items:me',
    'read:items:me',
    'write:items',
    'read:items',
    'read:groups:associated',
    'write:groupmemberships:me',
]

def get_token_info_dev(token: str):
    mock = {
        'uid': 'auth0|643db743a891bec857308e2f',
        'sub': "auth0|643db743a891bec857308e2f",
        'scopes': ALL_SCOPES
    }

    return mock


def info_from_admin(token):
    """
    Validate and decode token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    'scope' or 'scopes' will be passed to scope validation function.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """

    return get_token_info(token)


def validate_scope_admin(required_scopes, token_scopes):
    """
    Validate required scopes are included in token scope

    :param required_scopes Required scope to access called API
    :type required_scopes: List[str]
    :param token_scopes Scope present in token
    :type token_scopes: List[str]
    :return: True if access to called API is allowed
    :rtype: bool
    """
    return set(required_scopes).issubset(set(token_scopes))


def info_from_standard(token):
    """
    Validate and decode token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    'scope' or 'scopes' will be passed to scope validation function.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    
    return get_token_info(token)


def validate_scope_standard(required_scopes, token_scopes):
    """
    Validate required scopes are included in token scope

    :param required_scopes Required scope to access called API
    :type required_scopes: List[str]
    :param token_scopes Scope present in token
    :type token_scopes: List[str]
    :return: True if access to called API is allowed
    :rtype: bool
    """
    return set(required_scopes).issubset(set(token_scopes))


def info_from_staff(token):
    """
    Validate and decode token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    'scope' or 'scopes' will be passed to scope validation function.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    
    return get_token_info(token)


def validate_scope_staff(required_scopes, token_scopes):
    """
    Validate required scopes are included in token scope

    :param required_scopes Required scope to access called API
    :type required_scopes: List[str]
    :param token_scopes Scope present in token
    :type token_scopes: List[str]
    :return: True if access to called API is allowed
    :rtype: bool
    """
    return set(required_scopes).issubset(set(token_scopes))

