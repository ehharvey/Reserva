import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.unavailabilities_id_delete200_response import UnavailabilitiesIdDelete200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_put200_response import UnavailabilitiesIdPut200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_put400_response import UnavailabilitiesIdPut400Response  # noqa: E501
from openapi_server.models.unavailabilities_post201_response import UnavailabilitiesPost201Response  # noqa: E501
from openapi_server.models.unavailabilities_post400_response import UnavailabilitiesPost400Response  # noqa: E501
from openapi_server.models.unavailabilities_post_request import UnavailabilitiesPostRequest  # noqa: E501
from openapi_server import util


def unavailabilities_id_delete(id):  # noqa: E501
    """Delete an unavailability

     # noqa: E501

    :param id: the unavailability id
    :type id: str
    :type id: str

    :rtype: Union[UnavailabilitiesIdDelete200Response, Tuple[UnavailabilitiesIdDelete200Response, int], Tuple[UnavailabilitiesIdDelete200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def unavailabilities_id_put(id):  # noqa: E501
    """update an unavailability

     # noqa: E501

    :param id: the unavailability id
    :type id: str
    :type id: str

    :rtype: Union[UnavailabilitiesIdPut200Response, Tuple[UnavailabilitiesIdPut200Response, int], Tuple[UnavailabilitiesIdPut200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def unavailabilities_post(unavailabilities_post_request=None):  # noqa: E501
    """Create a new unavailability

     # noqa: E501

    :param unavailabilities_post_request: 
    :type unavailabilities_post_request: dict | bytes

    :rtype: Union[UnavailabilitiesPost201Response, Tuple[UnavailabilitiesPost201Response, int], Tuple[UnavailabilitiesPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        unavailabilities_post_request = UnavailabilitiesPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    
    return 'do some magic!'
