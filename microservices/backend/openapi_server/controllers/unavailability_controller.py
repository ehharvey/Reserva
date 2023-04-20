import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.unavailabilities_get200_response import UnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_delete200_response import UnavailabilitiesIdDelete200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_get200_response import UnavailabilitiesIdGet200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_get400_response import UnavailabilitiesIdGet400Response  # noqa: E501
from openapi_server.models.unavailabilities_id_put200_response import UnavailabilitiesIdPut200Response  # noqa: E501
from openapi_server.models.unavailabilities_post_request import UnavailabilitiesPostRequest  # noqa: E501
from openapi_server import util


def unavailabilities_get():  # noqa: E501
    """unavailabilities_get

    Retrieve all unavailability associated with a student or a room. # noqa: E501


    :rtype: Union[UnavailabilitiesGet200Response, Tuple[UnavailabilitiesGet200Response, int], Tuple[UnavailabilitiesGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def unavailabilities_id_delete(id):  # noqa: E501
    """unavailabilities_id_delete

    Delete a specific unavailability identified by the &#x60;id&#x60; parameter. # noqa: E501

    :param id: The unavailability ID
    :type id: str
    :type id: str

    :rtype: Union[UnavailabilitiesIdDelete200Response, Tuple[UnavailabilitiesIdDelete200Response, int], Tuple[UnavailabilitiesIdDelete200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def unavailabilities_id_get(id):  # noqa: E501
    """unavailabilities_id_get

    Retrieves information about a specific unavailability identified by the &#x60;id&#x60; parameter. # noqa: E501

    :param id: The unavailability ID
    :type id: str
    :type id: str

    :rtype: Union[UnavailabilitiesIdGet200Response, Tuple[UnavailabilitiesIdGet200Response, int], Tuple[UnavailabilitiesIdGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def unavailabilities_id_put(id):  # noqa: E501
    """unavailabilities_id_put

    Update a specific unavailability identified by the &#x60;id&#x60; parameter with the information  provided in the request body.  # noqa: E501

    :param id: The unavailability ID
    :type id: str
    :type id: str

    :rtype: Union[UnavailabilitiesIdPut200Response, Tuple[UnavailabilitiesIdPut200Response, int], Tuple[UnavailabilitiesIdPut200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def unavailabilities_post(unavailabilities_post_request=None):  # noqa: E501
    """unavailabilities_post

     # noqa: E501

    :param unavailabilities_post_request: 
    :type unavailabilities_post_request: dict | bytes

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        unavailabilities_post_request = UnavailabilitiesPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
