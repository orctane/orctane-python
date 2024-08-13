from .request import Request


def get(path: str, params: dict = None) -> dict:
    """Get makes a GET request to the API.

    Args:
        path (str): The path to the API endpoint.
        params (dict, optional): The parameters to include in the request. Defaults to None.

    Returns:
        dict: The response from the API.
    """
    handler = Request(method="get", path=path, params=params, body=None)
    return handler.handle()


def post(path: str, body: dict) -> dict:
    """Post makes a POST request to the API.

    Args:
        path (str): The path to the API endpoint.
        body (dict): The body of the request.

    Returns:
        dict: The response from the API.
    """
    handler = Request(method="post", path=path, params=None, body=body)
    return handler.handle()


def put(path: str, body: dict) -> dict:
    """Put makes a PUT request to the API.

    Args:
        path (str): The path to the API endpoint.
        body (dict): The body of the request.

    Returns:
        dict: The response from the API.
    """
    handler = Request(method="put", path=path, params=None, body=body)
    return handler.handle()


def patch(path: str, body: dict) -> dict:
    """Patch makes a PATCH request to the API.

    Args:
        path (str): The path to the API endpoint.
        body (dict): The body of the request.

    Returns:
        dict: The response from the API.
    """
    handler = Request(method="patch", path=path, params=None, body=body)
    return handler.handle()


def delete(path: str, params: dict = None) -> dict:
    """Delete makes a DELETE request to the API.

    Args:
        path (str): The path to the API endpoint.
        params (dict, optional): The parameters to include in the request. Defaults to None.

    Returns:
        dict: The response from the API.
    """
    handler = Request(method="delete", path=path, params=params, body=None)
    return handler.handle()
