import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.items_get200_response import ItemsGet200Response  # noqa: E501
from openapi_server.models.items_post201_response import ItemsPost201Response  # noqa: E501
from openapi_server.models.new_item import NewItem  # noqa: E501
from openapi_server import util


def items_get(page=None, per_page=None, name_search=None, location_search=None, description_search=None):  # noqa: E501
    """gets a list of items. for now, the only kind of item is a room.

     # noqa: E501

    :param page: Page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param name_search: Search for a room by name
    :type name_search: str
    :param location_search: Search for a room by location
    :type location_search: str
    :param description_search: Search for a room by description
    :type description_search: str

    :rtype: Union[ItemsGet200Response, Tuple[ItemsGet200Response, int], Tuple[ItemsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_id_delete(id):  # noqa: E501
    """delete a room object

     # noqa: E501

    :param id: item id
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_id_put(id, item=None):  # noqa: E501
    """updates an item. for now, the only kind of item is a room.

     # noqa: E501

    :param id: item id
    :type id: int
    :param item: 
    :type item: dict | bytes

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_id_unavailabilities_get(id, start, end, page=None, per_page=None):  # noqa: E501
    """gets a list of unavailabilities for a given item.

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str
    :param start: the start date of the unavailabilities to get
    :type start: str
    :param end: the end date of the unavailabilities to get
    :type end: str
    :param page: the page of unavailabilities to get
    :type page: int
    :param per_page: the number of unavailabilities to get per page
    :type per_page: int

    :rtype: Union[GroupsIdUnavailabilitiesGet200Response, Tuple[GroupsIdUnavailabilitiesGet200Response, int], Tuple[GroupsIdUnavailabilitiesGet200Response, int, Dict[str, str]]
    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
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
