# chatt_client.DefaultApi

All URIs are relative to */chat_telegram/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_health_get**](DefaultApi.md#health_check_health_get) | **GET** /health | Health Check


# **health_check_health_get**
> HealthCheckResponse health_check_health_get()

Health Check

### Example


```python
import chatt_client
from chatt_client.models.health_check_response import HealthCheckResponse
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
    api_instance = chatt_client.DefaultApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_health_get()
        print("The response of DefaultApi->health_check_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
