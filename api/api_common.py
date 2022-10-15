from fastapi import Response
from bson.objectid import ObjectId


def find_all_id_query(objs):
    return {'_id': {'$in': [obj.id for obj in objs]}}


def pack_response(response: Response, status: int, message: str, data: dict = None):
    default = {"status": status, "msg": message}
    response.status_code = status
    if data is None:
        return default
    else:
        return {**default, **data}
