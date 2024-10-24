# chatt_client.SettingApi

All URIs are relative to */chat_telegram/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_telegram_by_phone_setting_auth_code_post**](SettingApi.md#auth_telegram_by_phone_setting_auth_code_post) | **POST** /setting/auth/{code} | Auth Telegram By Phone
[**auth_telegram_by_phone_setting_auth_post**](SettingApi.md#auth_telegram_by_phone_setting_auth_post) | **POST** /setting/auth | Auth Telegram By Phone
[**auth_telegram_by_phone_v1_setting_auth_code_post**](SettingApi.md#auth_telegram_by_phone_v1_setting_auth_code_post) | **POST** /v1/setting/auth/{code} | Auth Telegram By Phone
[**auth_telegram_by_phone_v1_setting_auth_post**](SettingApi.md#auth_telegram_by_phone_v1_setting_auth_post) | **POST** /v1/setting/auth | Auth Telegram By Phone


# **auth_telegram_by_phone_setting_auth_code_post**
> bool auth_telegram_by_phone_setting_auth_code_post(code, x_request_id=x_request_id)

Auth Telegram By Phone

### Example


```python
import chatt_client
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
    api_instance = chatt_client.SettingApi(api_client)
    code = 'code_example' # str | 
    x_request_id = '8955873c-40f1-429c-aa46-1e63ace8967d' # str |  (optional) (default to '8955873c-40f1-429c-aa46-1e63ace8967d')

    try:
        # Auth Telegram By Phone
        api_response = api_instance.auth_telegram_by_phone_setting_auth_code_post(code, x_request_id=x_request_id)
        print("The response of SettingApi->auth_telegram_by_phone_setting_auth_code_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingApi->auth_telegram_by_phone_setting_auth_code_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;8955873c-40f1-429c-aa46-1e63ace8967d&#39;]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **auth_telegram_by_phone_setting_auth_post**
> bool auth_telegram_by_phone_setting_auth_post(x_request_id=x_request_id)

Auth Telegram By Phone

### Example


```python
import chatt_client
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
    api_instance = chatt_client.SettingApi(api_client)
    x_request_id = '8955873c-40f1-429c-aa46-1e63ace8967d' # str |  (optional) (default to '8955873c-40f1-429c-aa46-1e63ace8967d')

    try:
        # Auth Telegram By Phone
        api_response = api_instance.auth_telegram_by_phone_setting_auth_post(x_request_id=x_request_id)
        print("The response of SettingApi->auth_telegram_by_phone_setting_auth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingApi->auth_telegram_by_phone_setting_auth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**|  | [optional] [default to &#39;8955873c-40f1-429c-aa46-1e63ace8967d&#39;]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **auth_telegram_by_phone_v1_setting_auth_code_post**
> bool auth_telegram_by_phone_v1_setting_auth_code_post(code, x_request_id=x_request_id)

Auth Telegram By Phone

### Example

* Bearer Authentication (HTTPBearer):

```python
import chatt_client
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
    api_instance = chatt_client.SettingApi(api_client)
    code = 'code_example' # str | 
    x_request_id = '8955873c-40f1-429c-aa46-1e63ace8967d' # str |  (optional) (default to '8955873c-40f1-429c-aa46-1e63ace8967d')

    try:
        # Auth Telegram By Phone
        api_response = api_instance.auth_telegram_by_phone_v1_setting_auth_code_post(code, x_request_id=x_request_id)
        print("The response of SettingApi->auth_telegram_by_phone_v1_setting_auth_code_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingApi->auth_telegram_by_phone_v1_setting_auth_code_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **x_request_id** | **str**|  | [optional] [default to &#39;8955873c-40f1-429c-aa46-1e63ace8967d&#39;]

### Return type

**bool**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **auth_telegram_by_phone_v1_setting_auth_post**
> bool auth_telegram_by_phone_v1_setting_auth_post(x_request_id=x_request_id)

Auth Telegram By Phone

### Example

* Bearer Authentication (HTTPBearer):

```python
import chatt_client
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
    api_instance = chatt_client.SettingApi(api_client)
    x_request_id = '8955873c-40f1-429c-aa46-1e63ace8967d' # str |  (optional) (default to '8955873c-40f1-429c-aa46-1e63ace8967d')

    try:
        # Auth Telegram By Phone
        api_response = api_instance.auth_telegram_by_phone_v1_setting_auth_post(x_request_id=x_request_id)
        print("The response of SettingApi->auth_telegram_by_phone_v1_setting_auth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingApi->auth_telegram_by_phone_v1_setting_auth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**|  | [optional] [default to &#39;8955873c-40f1-429c-aa46-1e63ace8967d&#39;]

### Return type

**bool**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

