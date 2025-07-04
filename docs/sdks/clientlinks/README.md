# ClientLinks
(*client_links*)

## Overview

### Available Operations

* [create](#create) - Create client link

## create

Link a new or existing organization to your OAuth application, in effect creating a new client. The response contains a `clientLink` where you should redirect your customer to.

The `clientLink` URL behaves similar to the regular OAuth authorization URL. It supports the following parameters from the [Authorize](authorize) endpoint:

* `client_id`
* `state`
* `approval_prompt`
* `scope`

We recommend at least requesting the scopes `onboarding.read onboarding.write` this way.

Error handling is also dealt with similar to the [Authorize](authorize) endpoint: the customer is redirected back to your app's redirect URL with the `error` and `error_description` parameters added to the URL.

> 🔑 Access with
>
> [Access token with **clients.write**](/reference/authentication)

### Example Usage

```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.client_links.create(request={
        "owner": {
            "email": "john@example.org",
            "given_name": "John",
            "family_name": "Doe",
            "locale": "en_US",
        },
        "name": "Acme Corporation",
        "address": {
            "street_and_number": "Main Street 123",
            "postal_code": "1234AB",
            "city": "Amsterdam",
            "country": "NL",
        },
        "registration_number": "12345678",
        "vat_number": "123456789B01",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CreateClientLinkRequestBody](../../models/createclientlinkrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.CreateClientLinkResponseBody](../../models/createclientlinkresponsebody.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| models.CreateClientLinkClientLinksResponseBody         | 404                                                    | application/hal+json                                   |
| models.CreateClientLinkClientLinksResponseResponseBody | 422                                                    | application/hal+json                                   |
| models.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |