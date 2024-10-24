# coding: utf-8

"""
    Chat Telegram Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import StrictStr
from typing import Optional
from chatt_client.models.message_schema import MessageSchema
from chatt_client.models.message_schema_sent import MessageSchemaSent

from chatt_client.api_client import ApiClient, RequestSerialized
from chatt_client.api_response import ApiResponse
from chatt_client.rest import RESTResponseType


class SupportApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def send_message_telegram_support_users_user_id_setting_setting_id_post(
        self,
        user_id: StrictStr,
        setting_id: StrictStr,
        message_schema: MessageSchema,
        x_request_id: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MessageSchemaSent:
        """Send Message Telegram


        :param user_id: (required)
        :type user_id: str
        :param setting_id: (required)
        :type setting_id: str
        :param message_schema: (required)
        :type message_schema: MessageSchema
        :param x_request_id:
        :type x_request_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._send_message_telegram_support_users_user_id_setting_setting_id_post_serialize(
            user_id=user_id,
            setting_id=setting_id,
            message_schema=message_schema,
            x_request_id=x_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MessageSchemaSent",
            '400': "ServiceErrorPydantic",
            '401': "ServiceErrorPydantic",
            '403': "ServiceErrorPydantic",
            '404': "ServiceErrorPydantic",
            '409': "ServiceErrorPydantic",
            '422': None,
            '500': "ServiceErrorPydantic",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def send_message_telegram_support_users_user_id_setting_setting_id_post_with_http_info(
        self,
        user_id: StrictStr,
        setting_id: StrictStr,
        message_schema: MessageSchema,
        x_request_id: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MessageSchemaSent]:
        """Send Message Telegram


        :param user_id: (required)
        :type user_id: str
        :param setting_id: (required)
        :type setting_id: str
        :param message_schema: (required)
        :type message_schema: MessageSchema
        :param x_request_id:
        :type x_request_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._send_message_telegram_support_users_user_id_setting_setting_id_post_serialize(
            user_id=user_id,
            setting_id=setting_id,
            message_schema=message_schema,
            x_request_id=x_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MessageSchemaSent",
            '400': "ServiceErrorPydantic",
            '401': "ServiceErrorPydantic",
            '403': "ServiceErrorPydantic",
            '404': "ServiceErrorPydantic",
            '409': "ServiceErrorPydantic",
            '422': None,
            '500': "ServiceErrorPydantic",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def send_message_telegram_support_users_user_id_setting_setting_id_post_without_preload_content(
        self,
        user_id: StrictStr,
        setting_id: StrictStr,
        message_schema: MessageSchema,
        x_request_id: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Send Message Telegram


        :param user_id: (required)
        :type user_id: str
        :param setting_id: (required)
        :type setting_id: str
        :param message_schema: (required)
        :type message_schema: MessageSchema
        :param x_request_id:
        :type x_request_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._send_message_telegram_support_users_user_id_setting_setting_id_post_serialize(
            user_id=user_id,
            setting_id=setting_id,
            message_schema=message_schema,
            x_request_id=x_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MessageSchemaSent",
            '400': "ServiceErrorPydantic",
            '401': "ServiceErrorPydantic",
            '403': "ServiceErrorPydantic",
            '404': "ServiceErrorPydantic",
            '409': "ServiceErrorPydantic",
            '422': None,
            '500': "ServiceErrorPydantic",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _send_message_telegram_support_users_user_id_setting_setting_id_post_serialize(
        self,
        user_id,
        setting_id,
        message_schema,
        x_request_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['user_id'] = user_id
        if setting_id is not None:
            _path_params['setting_id'] = setting_id
        # process the query parameters
        # process the header parameters
        if x_request_id is not None:
            _header_params['x-request-id'] = x_request_id
        # process the form parameters
        # process the body parameter
        if message_schema is not None:
            _body_params = message_schema


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/support/users/{user_id}/setting/{setting_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def send_message_telegram_v1_support_users_user_id_setting_setting_id_post(
        self,
        user_id: StrictStr,
        setting_id: StrictStr,
        message_schema: MessageSchema,
        x_request_id: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MessageSchemaSent:
        """Send Message Telegram


        :param user_id: (required)
        :type user_id: str
        :param setting_id: (required)
        :type setting_id: str
        :param message_schema: (required)
        :type message_schema: MessageSchema
        :param x_request_id:
        :type x_request_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._send_message_telegram_v1_support_users_user_id_setting_setting_id_post_serialize(
            user_id=user_id,
            setting_id=setting_id,
            message_schema=message_schema,
            x_request_id=x_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MessageSchemaSent",
            '400': "ServiceErrorPydantic",
            '401': "ServiceErrorPydantic",
            '403': "ServiceErrorPydantic",
            '404': "ServiceErrorPydantic",
            '409': "ServiceErrorPydantic",
            '422': None,
            '500': "ServiceErrorPydantic",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def send_message_telegram_v1_support_users_user_id_setting_setting_id_post_with_http_info(
        self,
        user_id: StrictStr,
        setting_id: StrictStr,
        message_schema: MessageSchema,
        x_request_id: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MessageSchemaSent]:
        """Send Message Telegram


        :param user_id: (required)
        :type user_id: str
        :param setting_id: (required)
        :type setting_id: str
        :param message_schema: (required)
        :type message_schema: MessageSchema
        :param x_request_id:
        :type x_request_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._send_message_telegram_v1_support_users_user_id_setting_setting_id_post_serialize(
            user_id=user_id,
            setting_id=setting_id,
            message_schema=message_schema,
            x_request_id=x_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MessageSchemaSent",
            '400': "ServiceErrorPydantic",
            '401': "ServiceErrorPydantic",
            '403': "ServiceErrorPydantic",
            '404': "ServiceErrorPydantic",
            '409': "ServiceErrorPydantic",
            '422': None,
            '500': "ServiceErrorPydantic",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def send_message_telegram_v1_support_users_user_id_setting_setting_id_post_without_preload_content(
        self,
        user_id: StrictStr,
        setting_id: StrictStr,
        message_schema: MessageSchema,
        x_request_id: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Send Message Telegram


        :param user_id: (required)
        :type user_id: str
        :param setting_id: (required)
        :type setting_id: str
        :param message_schema: (required)
        :type message_schema: MessageSchema
        :param x_request_id:
        :type x_request_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._send_message_telegram_v1_support_users_user_id_setting_setting_id_post_serialize(
            user_id=user_id,
            setting_id=setting_id,
            message_schema=message_schema,
            x_request_id=x_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MessageSchemaSent",
            '400': "ServiceErrorPydantic",
            '401': "ServiceErrorPydantic",
            '403': "ServiceErrorPydantic",
            '404': "ServiceErrorPydantic",
            '409': "ServiceErrorPydantic",
            '422': None,
            '500': "ServiceErrorPydantic",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _send_message_telegram_v1_support_users_user_id_setting_setting_id_post_serialize(
        self,
        user_id,
        setting_id,
        message_schema,
        x_request_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['user_id'] = user_id
        if setting_id is not None:
            _path_params['setting_id'] = setting_id
        # process the query parameters
        # process the header parameters
        if x_request_id is not None:
            _header_params['x-request-id'] = x_request_id
        # process the form parameters
        # process the body parameter
        if message_schema is not None:
            _body_params = message_schema


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/support/users/{user_id}/setting/{setting_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


