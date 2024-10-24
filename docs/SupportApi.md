# chatt_client.SupportApi

All URIs are relative to */chat_telegram/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_message_telegram_support_users_user_id_setting_setting_id_post**](SupportApi.md#send_message_telegram_support_users_user_id_setting_setting_id_post) | **POST** /support/users/{user_id}/setting/{setting_id} | Send Message Telegram
[**send_message_telegram_v1_support_users_user_id_setting_setting_id_post**](SupportApi.md#send_message_telegram_v1_support_users_user_id_setting_setting_id_post) | **POST** /v1/support/users/{user_id}/setting/{setting_id} | Send Message Telegram


# **send_message_telegram_support_users_user_id_setting_setting_id_post**
> MessageSchemaSent send_message_telegram_support_users_user_id_setting_setting_id_post(user_id, setting_id, message_schema, x_request_id=x_request_id)

Send Message Telegram

### Example


```python
import chatt_client
from chatt_client.models.message_schema import MessageSchema
from chatt_client.models.message_schema_sent import MessageSchemaSent
from chatt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /chat_telegram/api
# See configuration.py for a list of all supported configuration parameters.
configuration = chatt_client.Configuration(
    host = "/chat_telegram/api"
)


# Enter a context with an instance of the API client
with chatt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chatt_client.SupportApi(api_client)
    user_id = 'user_id_example' # str | 
    setting_id = 'setting_id_example' # str | 
    message_schema = chatt_client.MessageSchema() # MessageSchema | 
    x_request_id = '8955873c-40f1-429c-aa46-1e63ace8967d' # str |  (optional) (default to '8955873c-40f1-429c-aa46-1e63ace8967d')

    try:
        # Send Message Telegram
        api_response = api_instance.send_message_telegram_support_users_user_id_setting_setting_id_post(user_id, setting_id, message_schema, x_request_id=x_request_id)
        print("The response of SupportApi->send_message_telegram_support_users_user_id_setting_setting_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->send_message_telegram_support_users_user_id_setting_setting_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **setting_id** | **str**|  | 
 **message_schema** | [**MessageSchema**](MessageSchema.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;8955873c-40f1-429c-aa46-1e63ace8967d&#39;]

### Return type

[**MessageSchemaSent**](MessageSchemaSent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message_telegram_v1_support_users_user_id_setting_setting_id_post**
> MessageSchemaSent send_message_telegram_v1_support_users_user_id_setting_setting_id_post(user_id, setting_id, message_schema, x_request_id=x_request_id)

Send Message Telegram

### Example

* Bearer Authentication (HTTPBearer):

```python
import chatt_client
from chatt_client.models.message_schema import MessageSchema
from chatt_client.models.message_schema_sent import MessageSchemaSent
from chatt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /chat_telegram/api
# See configuration.py for a list of all supported configuration parameters.
configuration = chatt_client.Configuration(
    host = "/chat_telegram/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = chatt_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with chatt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chatt_client.SupportApi(api_client)
    user_id = 'user_id_example' # str | 
    setting_id = 'setting_id_example' # str | 
    message_schema = chatt_client.MessageSchema() # MessageSchema | 
    x_request_id = '8955873c-40f1-429c-aa46-1e63ace8967d' # str |  (optional) (default to '8955873c-40f1-429c-aa46-1e63ace8967d')

    try:
        # Send Message Telegram
        api_response = api_instance.send_message_telegram_v1_support_users_user_id_setting_setting_id_post(user_id, setting_id, message_schema, x_request_id=x_request_id)
        print("The response of SupportApi->send_message_telegram_v1_support_users_user_id_setting_setting_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->send_message_telegram_v1_support_users_user_id_setting_setting_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **setting_id** | **str**|  | 
 **message_schema** | [**MessageSchema**](MessageSchema.md)|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;8955873c-40f1-429c-aa46-1e63ace8967d&#39;]

### Return type

[**MessageSchemaSent**](MessageSchemaSent.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

