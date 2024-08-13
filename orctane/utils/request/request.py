from typing import Literal, Any, Dict, Generic, List, Union, cast, TypeVar
import requests
from requests import Response

import orctane
from orctane.utils.exceptions import raise_exception
from orctane.utils.version import get_version

RequestMethods = Literal["get", "post", "put", "patch", "delete"]

T = TypeVar("T")


def get_headers() -> Dict[Any, Any]:
    """get_headers returns the HTTP headers that will be
    used for every req.

    Returns:
        Dict: configured HTTP Headers
    """
    return {
        "Accept": "application/json",
        "Authorization": f"Bearer {orctane.api_key}",
        "User-Agent": f"orctane-python:{get_version()}",
    }


class Request(Generic[T]):
    """Request is a generic class that handles the request to the Orctane API.
    Args:
        method (RequestMethods): The HTTP method to use for the request.
        path (str): The path to the endpoint.
        params (Union[Dict[Any, Any], List[Dict[Any, Any]]]): The parameters to include in the request.
        body (Any): The body to include in the request.
        """

    def __init__(self, method: RequestMethods, path: str, params: Union[Dict[Any, Any], List[Dict[Any, Any]]] | None = None,
                 body: Dict[Any, Any] | None = None):


        self.method = method
        self.path = path
        self.params = params
        self.body = body

    def handle(self) -> Union[T, None]:
        """handle makes the request to the API.
        Returns:
            Response: The response from the API.
        """
        url = f"{orctane.api_url}{self.path}"
        response = self.make_request(url=url)

        # this is a safety net, if we get here it means the Orctane API is having issues
        # and most likely the gateway is returning htmls
        if "application/json" not in response.headers["content-type"]:
            raise_exception(
                code=500,
                message="Failed to parse Orctane API response. Please try again.",
                error_type="InternalServerError",
            )

        # handle error in case there is a statusCode attr present
        # and status != 200 and response is a json.
        if response.status_code != 200 and response.json().get("status_code"):
            error = response.json()
            raise_exception(
                code=error.get("status_code"),
                message=error.get("message"),
                error_type=error.get("name"),
            )

        return cast(T, response.json())

    def make_request(self, url: str, **kwargs) -> Response:
        """Makes a request to the API.

        Args:
            url (str): The URL to make the request to.
            headers (Dict[str, str]): The headers to include in the request.
            **kwargs: Additional keyword arguments to pass to the request.

        Returns:
            Dict[str, Any]: The response from the API.
            :param url: The URL to make the request to.
        Returns:
            Response: The response from the API.
        """
        headers = get_headers()
        params = self.params
        method = self.method

        response = requests.request(
            method,
            url=url,
            headers=headers,
            params=params,
            json=self.body,
        )

        try:
            return requests.request(method=method, url=url, headers=headers, params=params, json=self.body)
        except requests.HTTPError as e:
            raise e
