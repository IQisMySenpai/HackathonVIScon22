

def pack_response(status: int, message: str, data: dict = None):
    default = {"status": status, "msg": message}
    if data is None:
        return default
    else:
        return {**default, **data}
