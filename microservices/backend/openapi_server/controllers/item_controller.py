import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.items_get200_response import ItemsGet200Response  # noqa: E501
from openapi_server.models.items_id_unavailabilities_get200_response import ItemsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.items_post201_response import ItemsPost201Response  # noqa: E501
from openapi_server.models.new_item import NewItem  # noqa: E501
from openapi_server import util


def items_get():  # noqa: E501
    """gets a list of items. for now, the only kind of item is a room.

     # noqa: E501


    :rtype: Union[ItemsGet200Response, Tuple[ItemsGet200Response, int], Tuple[ItemsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_id_delete(id):  # noqa: E501
    """delete a room object

     # noqa: E501

    :param id: user id
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_id_put(id, item=None):  # noqa: E501
    """updates an item. for now, the only kind of item is a room.

     # noqa: E501

    :param id: user id
    :type id: int
    :param item: 
    :type item: dict | bytes

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_id_unavailabilities_get(id):  # noqa: E501
    """gets a list of unavailabilities for a given item.

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[ItemsIdUnavailabilitiesGet200Response, Tuple[ItemsIdUnavailabilitiesGet200Response, int], Tuple[ItemsIdUnavailabilitiesGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_post(new_item=None):  # noqa: E501
    """posts an item. for now, the only kind of item is a room.

     # noqa: E501

    :param new_item: 
    :type new_item: dict | bytes

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_item = NewItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
