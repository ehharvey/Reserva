from enum import Enum
from pydantic import BaseModel

class AuthenticationBackend(Enum):
    """
    Configuration for the authentication backend
    Currently only Auth0 is supported
    """
    Auth0 = "auth0"
    

class Auth0Config(BaseModel):
    """Configuration for the authentication"""
    auth0_domain: str
    api_token: str

class Config(BaseModel):
    """Configuration for the application"""
    authentication: Auth0Config
    
