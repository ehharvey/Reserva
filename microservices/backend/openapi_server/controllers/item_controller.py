from bson import ObjectId
import connexion
from pymongo import MongoClient
import six
from typing import Dict
from typing import Tuple
from typing import Union
from openapi_server.models.update_item import UpdateItem
from openapi_server.models.user import User
from openapi_server.user_utils import get_user_details
from openapi_server.db_utils import create_item

from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.items_get200_response import ItemsGet200Response  # noqa: E501
from openapi_server.models.items_post201_response import ItemsPost201Response  # noqa: E501
from openapi_server.models.new_item import NewItem  # noqa: E501
from openapi_server import util
from openapi_server.db_utils import get_model_from_mongo


def items_get(client: MongoClient, page=None, per_page=None, name_search=None, location_search=None, description_search=None):  # noqa: E501
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

    db = client["main"]
    items = db["items"]

    find = items.find().sort("_id")

    # TODO: input validation/sanitization
    if name_search:
        find = find.where(f'this.name.toLowerCase().includes("{name_search.lower()}")')
    
    if location_search:
        find = find.where(f'this.location.toLowerCase().includes("{location_search.lower()}")')
    
    if description_search:
        find = find.where(f'this.description.toLowerCase().includes("{description_search.lower()}")')

    if page:
        find = find.skip((page - 1) * per_page)


    if per_page:
        find = find.limit(per_page)

    result = [
        get_model_from_mongo(item)
        for item in find
    ]

    return ItemsGet200Response(
        rooms=result
    )


def items_id_delete(id_, db: MongoClient, **kwargs):  # noqa: E501
    """delete a room object

     # noqa: E501

    :param id: item id
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    main = db["main"]
    items = main["items"]

    id_ = ObjectId(id_)

    # get the item
    item = items.find_one({"_id": id_})

    if not item:
        return "Not Found", 404
    else:
        items.delete_one({"_id": id_})
        return "Deleted", 204
    


def items_id_put(client: MongoClient, id_, item=None):  # noqa: E501
    """updates an item. for now, the only kind of item is a room.

     # noqa: E501

    :param id: item id
    :type id: int
    :param item: 
    :type item: dict | bytes

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    id_ = ObjectId(id_)

    if connexion.request.is_json:
        item = UpdateItem.from_dict(connexion.request.get_json())  # noqa: E501

        # Find item from database
        db = client["main"]
        items = db["items"]
        item_to_update = items.find_one({"_id": id_})

        if not item_to_update:
            return "Not Found", 404
        else:
            items.update_one({"_id": id_}, {"$set": item.to_dict()})
            return ItemsPost201Response(room=item)


def items_id_unavailabilities_get(client: MongoClient, id_, start=None, end=None, page=None, per_page=None):  # noqa: E501
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

    db = client["main"]
    items = db["items"]
    unavailabilities = db["unavailabilities"]

    id_ = ObjectId(id_)

    # get the item
    item = items.find_one({"_id": id_})

    if not item:
        return "Not Found", 404
    else:
        # get the unavailabilities
        find = unavailabilities.find({
            "item": id_,
            "start": {
                "$gte": start,
                "$lte": end
            }
        }).sort("start")

        if page:
            find = find.skip((page - 1) * per_page)

        if per_page:
            find = find.limit(per_page)

        result = [
            get_model_from_mongo(unavailability)
            for unavailability in find
        ]

        return GroupsIdUnavailabilitiesGet200Response(
            unavailabilities=result
        )


def items_post(new_item=None):  # noqa: E501
    """posts an item. for now, the only kind of item is a room.

     # noqa: E501

    :param new_item: 
    :type new_item: dict | bytes

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_item = NewItem.from_dict(connexion.request.get_json())  # noqa: E501
        created = create_item(new_item)
        return ItemsPost201Response(room=created), 201
    else:
        return "Bad Request", 400
