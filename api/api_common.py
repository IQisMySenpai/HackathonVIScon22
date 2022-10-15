from fastapi import Response

def pack_response(response: Response, status: int, message: str, data: dict = None):
    default = {"status": status, "msg": message}
    response.status_code = status
    if data is None:
        return default
    else:
        return {**default, **data}
