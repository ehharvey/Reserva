import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.credit import Credit  # noqa: E501
from openapi_server.models.new_credit import NewCredit  # noqa: E501
from openapi_server.models.update_credit_by_id_request import UpdateCreditByIdRequest  # noqa: E501
from openapi_server import util


def create_credit(new_credit=None):  # noqa: E501
    """Create a new credit

     # noqa: E501

    :param new_credit: 
    :type new_credit: dict | bytes

    :rtype: Union[Credit, Tuple[Credit, int], Tuple[Credit, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_credit = NewCredit.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_credit_by_id(credit_id):  # noqa: E501
    """Delete a credit by ID

     # noqa: E501

    :param credit_id: The ID of the credit to delete.
    :type credit_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_credit_by_id(credit_id):  # noqa: E501
    """Get a credit by ID

     # noqa: E501

    :param credit_id: The ID of the credit to retrieve.
    :type credit_id: int

    :rtype: Union[Credit, Tuple[Credit, int], Tuple[Credit, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_credits():  # noqa: E501
    """Get all credits

     # noqa: E501


    :rtype: Union[List[Credit], Tuple[List[Credit], int], Tuple[List[Credit], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_credit_by_id(credit_id, update_credit_by_id_request=None):  # noqa: E501
    """Update a credit by ID

     # noqa: E501

    :param credit_id: The ID of the credit to update.
    :type credit_id: int
    :param update_credit_by_id_request: 
    :type update_credit_by_id_request: dict | bytes

    :rtype: Union[Credit, Tuple[Credit, int], Tuple[Credit, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_credit_by_id_request = UpdateCreditByIdRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
