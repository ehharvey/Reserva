from typing import List

from jwt import PyJWKClient
import jwt


# TODO: This is a temporary solution to get the scopes from the token
# REMOVE THIS ONCE WE HAVE A REAL AUTHENTICATION SYSTEM
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
    return {'scopes': ALL_SCOPES, 'uid': 'user_id'}


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
    # Validate and decode token as JWT
    # TODO: Have a global jwks that is injected into the function
    # jwks_client = PyJWKClient("https://DOMAIN.com/.well-known/jwks.json")
    # signing_key = jwks_client.get_signing_key_from_jwt(token)

    # claims = jwt.decode(
    #     token,
    #     signing_key.key,
    #     algorithms=["RS256"],
    #     # issuer="https://DOMAIN.com", # TODO: figure out how to verify issuer
    #     audience="http://localhost:8080"
    #     )
    
    # claims['scopes'] = claims['scope'].split(' ')

    return {'scopes': ALL_SCOPES, 'uid': 'user_id'}


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
    return {'scopes': ALL_SCOPES, 'uid': 'user_id'}


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

