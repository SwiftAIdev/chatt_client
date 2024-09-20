# chatt_client.SettingApi

All URIs are relative to */chat_telegram/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_telegram_by_phone_setting_auth_code_post**](SettingApi.md#auth_telegram_by_phone_setting_auth_code_post) | **POST** /setting/auth/{code} | Auth Telegram By Phone
[**auth_telegram_by_phone_setting_auth_post**](SettingApi.md#auth_telegram_by_phone_setting_auth_post) | **POST** /setting/auth | Auth Telegram By Phone


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
    x_request_id = '55d012f5-1dc6-4279-9af2-c561ce0ee7cb' # str |  (optional) (default to '55d012f5-1dc6-4279-9af2-c561ce0ee7cb')

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
 **x_request_id** | **str**|  | [optional] [default to &#39;55d012f5-1dc6-4279-9af2-c561ce0ee7cb&#39;]

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
    x_request_id = '55d012f5-1dc6-4279-9af2-c561ce0ee7cb' # str |  (optional) (default to '55d012f5-1dc6-4279-9af2-c561ce0ee7cb')

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
 **x_request_id** | **str**|  | [optional] [default to &#39;55d012f5-1dc6-4279-9af2-c561ce0ee7cb&#39;]

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

