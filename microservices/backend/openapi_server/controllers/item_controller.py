import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.items_get200_response import ItemsGet200Response  # noqa: E501
from openapi_server.models.items_id_put200_response import ItemsIdPut200Response  # noqa: E501
from openapi_server.models.items_post201_response import ItemsPost201Response  # noqa: E501
from openapi_server.models.new_item import NewItem  # noqa: E501
from openapi_server import util


def delete_room_id(id):  # noqa: E501
    """Delete a Room object existing in the Rooms resources

    ## More Information Request for &#x60;DELETE/rooms/{id}&#x60; requires an id  # noqa: E501

    :param id: User ID
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_get():  # noqa: E501
    """Gets a list of items. For now, the only kind of item is a room.

     # noqa: E501


    :rtype: Union[ItemsGet200Response, Tuple[ItemsGet200Response, int], Tuple[ItemsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_id_get(id):  # noqa: E501
    """Gets a Item object by id. For now, the only kind of item is a room.

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_id_put(id, item=None):  # noqa: E501
    """Updates an item. For now, the only kind of item is a room.

     # noqa: E501

    :param id: User ID
    :type id: int
    :param item: 
    :type item: dict | bytes

    :rtype: Union[ItemsIdPut200Response, Tuple[ItemsIdPut200Response, int], Tuple[ItemsIdPut200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_post(new_item=None):  # noqa: E501
    """Posts an item. For now, the only kind of item is a room.

     # noqa: E501

    :param new_item: 
    :type new_item: dict | bytes

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_item = NewItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
