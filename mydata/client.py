"""Client for myDATA's REST API.

This client supports a subset of myDATA's calls for **ERP**, as of API version
1.0.7 (1.0.8 dev).

Documentation: https://www.aade.gr/epiheiriseis/mydata-ilektronika-biblia-aade/mydata/tehnikes-prodiagrafes-ekdoseis-mydata
Testing environment: https://www.aade.gr/epiheiriseis/mydata-ilektronika-biblia-aade/mydata/dokimastiko-periballon

Supported calls:
* SendInvoice
* RequestDocs
* RequestTransmittedDocs

This client heavily relies on xsData for the XML serialization and parsing,
combined with the XSDs of IARP.
"""

import abc
import logging
import urllib.parse

import requests
import urllib3
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils.text import camel_case

from . import models_v1_0_9

MODELS_MODULE_DEV = models_v1_0_9
MODELS_MODULE_PROD = models_v1_0_9

BASE_URL_DEV = "https://mydataapidev.aade.gr/"
BASE_URL_PROD = "https://mydatapi.aade.gr/myDATA/"

HEADER_NAME_USER_ID = "aade-user-id"
HEADER_NAME_TOKEN = "ocp-apim-subscription-key"

PARAMS_REQUEST_DOCS = {
    "mark": {"required": True},
    "entity_vat_number": {},
    "date_from": {"type": "date"},
    "date_to": {"type": "date"},
    "receiver_vat_number": {},
    "inv_type": {},
    "max_mark": {},
    "next_partition_key": {},
    "next_row_key": {},
}

logger = logging.getLogger(__name__)


def parse(obj: str, cls) -> object:
    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(config=config, context=context)
    return parser.from_string(obj, cls)


def serialize(obj) -> str:
    config = SerializerConfig(pretty_print=True)
    serializer = XmlSerializer(config=config)
    return serializer.render(obj)


class Endpoint(abc.ABC):
    def __init__(self, prod=False):
        self.prod = prod
        self.models_module = (
            MODELS_MODULE_PROD if self.prod else MODELS_MODULE_DEV
        )

    @property
    @abc.abstractmethod
    def path(self):
        """The URL path for the endpoint."""

    @property
    @abc.abstractmethod
    def query_params(self):
        """The query parameters that this endpoint accepts."""

    @property
    @abc.abstractmethod
    def method(self):
        """The HTTP method for the endpoint."""

    @property
    @abc.abstractmethod
    def body_cls_name(self):
        """The name of the Python dataclass for the request's body."""

    @property
    @abc.abstractmethod
    def response_cls_name(self):
        """The name of the Python dataclass for the response's body."""

    @property
    def body_cls(self):
        """The Python dataclass for the request's body"""
        if self.body_cls_name is None:
            return None
        return getattr(self.models_module, self.body_cls_name)

    @property
    def response_cls(self):
        """The Python dataclass for the response's body"""
        if self.response_cls_name is None:
            return None
        return getattr(self.models_module, self.response_cls_name)

    def validate_request_body(self, body):
        if body is None:
            if self.body_cls:
                raise ValueError(
                    f"Endpoint {self.path} requires an HTTP request body:"
                    f" {self.body_cls}"
                )
        else:
            if self.body_cls is None:
                raise ValueError(
                    f"Endpoint {self.path} does not accept an HTTP"
                    f" request body: {type(body)}"
                )
            elif not isinstance(body, self.body_cls):
                raise ValueError(
                    f"Endpoint {self.path} requires a different HTTP"
                    f" request body. Expects {self.body_cls}, got {type(body)}"
                )


class SendInvoicesEndpoint(Endpoint):
    path = "SendInvoices"
    query_params = None
    method = "POST"
    body_cls_name = "InvoicesDoc"
    response_cls_name = "ResponseDoc"


class RequestDocsEndpoint(Endpoint):
    path = "RequestDocs"
    query_params = PARAMS_REQUEST_DOCS
    method = "GET"
    body_cls_name = None
    response_cls_name = "RequestedDoc"


class RequestTransmittedDocsEndpoint(Endpoint):
    path = "RequestTransmittedDocs"
    query_params = PARAMS_REQUEST_DOCS
    method = "GET"
    body_cls_name = None
    response_cls_name = "RequestedDoc"


class Client:
    def __init__(self, username: str, token: str, prod: bool):
        self.username = username
        self.token = token
        self.prod = prod

        self.base_url = BASE_URL_PROD if prod else BASE_URL_DEV
        self.auth_headers = {
            HEADER_NAME_USER_ID: self.username,
            HEADER_NAME_TOKEN: self.token,
            # Hide user agent
            "User-Agent": urllib3.util.SKIP_HEADER,
        }

        self.session = requests.Session()

    def request(
        self, method: str, url: str, params: dict | None = None, data=None
    ):
        req = requests.Request(
            method,
            url,
            headers=self.auth_headers,
            params=params,
            data=data,
        )
        prepped = req.prepare()
        resp = self.session.send(prepped)
        return resp

    def parse_params(self, accepted, params):
        recv_params = params.keys()
        accepted_params = accepted.keys()
        extra_params = set(recv_params) - set(accepted_params)
        missing_params = set(accepted_params) - set(recv_params)

        # Check if we got an extraneous HTTP parameter.
        if extra_params:
            msg = (
                f"Unexpected HTTP parameters: {extra_params}. Expected params"
                f" are: {accepted.keys()}"
            )
            raise ValueError(msg)

        # Check for required parameters.
        for p in missing_params:
            if accepted[p].get("required"):
                raise ValueError(f"Required parameter is missing: {p}")

        # Create the final HTTP params, ready for requests consumption
        return {camel_case(k): v for k, v in params.items()}

    def craft_url(self, path: str):
        return urllib.parse.urljoin(self.base_url, path)

    def request_endpoint(self, endpoint: Endpoint, body=None, **params):
        url = self.craft_url(endpoint.path)

        if endpoint.query_params:
            _params = self.parse_params(endpoint.query_params, params)
        else:
            _params = None

        if isinstance(body, str):
            # In that case, the user wants to send an XML.
            data = body
        else:
            # In that case, the user has a Python object and they want to send
            # it.
            endpoint.validate_request_body(body)
            data = None if body is None else serialize(body)

        resp = self.request(endpoint.method, url, params=_params, data=data)
        logger.debug(f"Response body: {resp.text}")

        if resp.status_code < 200 or resp.status_code >= 300:
            raise RuntimeError(
                f"The request to endpoint {endpoint.path} did not succeed."
                f" Received status code {resp.status_code}. Response body:"
                f" {resp.text}"
            )

        if resp.text is None:
            if endpoint.response_cls:
                raise ValueError(
                    f"Endpoint {endpoint.path} requires an HTTP response:"
                    f" {endpoint.response_cls}"
                )
            return None
        else:
            if endpoint.response_cls is None:
                raise ValueError(
                    f"Endpoint {endpoint.path} should not return an HTTP"
                    f" response body: {resp.text}"
                )
            else:
                parsed = parse(resp.text, endpoint.response_cls)
                parsed.xml = resp.text
                return parsed

    def send_invoices(self, invoices):
        endpoint = SendInvoicesEndpoint(self.prod)
        return self.request_endpoint(endpoint, body=invoices)

    def request_docs(self, **params):
        endpoint = RequestDocsEndpoint(self.prod)
        return self.request_endpoint(endpoint, **params)

    def request_transmitted_docs(self, **params):
        endpoint = RequestTransmittedDocsEndpoint(self.prod)
        return self.request_endpoint(endpoint, **params)
