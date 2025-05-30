"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from mollie import utils
from mollie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from mollie.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdatePaymentLinkMinimumAmountTypedDict(TypedDict):
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkMinimumAmount(BaseModel):
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkAllowedMethods(str, Enum):
    APPLEPAY = "applepay"
    BANCOMATPAY = "bancomatpay"
    BANCONTACT = "bancontact"
    BANKTRANSFER = "banktransfer"
    BELFIUS = "belfius"
    BLIK = "blik"
    CREDITCARD = "creditcard"
    EPS = "eps"
    GIFTCARD = "giftcard"
    IDEAL = "ideal"
    KBC = "kbc"
    MYBANK = "mybank"
    PAYBYBANK = "paybybank"
    PAYPAL = "paypal"
    PAYSAFECARD = "paysafecard"
    POINTOFSALE = "pointofsale"
    PRZELEWY24 = "przelewy24"
    SATISPAY = "satispay"
    TRUSTLY = "trustly"
    TWINT = "twint"


class UpdatePaymentLinkRequestBodyTypedDict(TypedDict):
    description: NotRequired[str]
    r"""A short description of the payment link. The description is visible in the Dashboard and will be shown on the customer's bank or card statement when possible.

    Updating the description does not affect any previously existing payments created for this payment link.
    """
    minimum_amount: NotRequired[UpdatePaymentLinkMinimumAmountTypedDict]
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""
    archived: NotRequired[bool]
    r"""Whether the payment link is archived. Customers will not be able to complete payments on archived payment links."""
    allowed_methods: NotRequired[Nullable[List[UpdatePaymentLinkAllowedMethods]]]
    r"""An array of payment methods that are allowed to be used for this payment link. When this parameter is not provided or is an empty array, all enabled payment methods will be available."""
    testmode: NotRequired[Nullable[bool]]
    r"""Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.

    Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.
    """


class UpdatePaymentLinkRequestBody(BaseModel):
    description: Optional[str] = None
    r"""A short description of the payment link. The description is visible in the Dashboard and will be shown on the customer's bank or card statement when possible.

    Updating the description does not affect any previously existing payments created for this payment link.
    """

    minimum_amount: Annotated[
        Optional[UpdatePaymentLinkMinimumAmount], pydantic.Field(alias="minimumAmount")
    ] = None
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""

    archived: Optional[bool] = None
    r"""Whether the payment link is archived. Customers will not be able to complete payments on archived payment links."""

    allowed_methods: Annotated[
        OptionalNullable[List[UpdatePaymentLinkAllowedMethods]],
        pydantic.Field(alias="allowedMethods"),
    ] = UNSET
    r"""An array of payment methods that are allowed to be used for this payment link. When this parameter is not provided or is an empty array, all enabled payment methods will be available."""

    testmode: OptionalNullable[bool] = UNSET
    r"""Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.

    Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "minimumAmount",
            "archived",
            "allowedMethods",
            "testmode",
        ]
        nullable_fields = ["allowedMethods", "testmode"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class UpdatePaymentLinkRequestTypedDict(TypedDict):
    payment_link_id: str
    r"""Provide the ID of the related payment link."""
    request_body: NotRequired[UpdatePaymentLinkRequestBodyTypedDict]


class UpdatePaymentLinkRequest(BaseModel):
    payment_link_id: Annotated[
        str,
        pydantic.Field(alias="paymentLinkId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Provide the ID of the related payment link."""

    request_body: Annotated[
        Optional[UpdatePaymentLinkRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class UpdatePaymentLinkPaymentLinksResponseDocumentationTypedDict(TypedDict):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str
    type: str


class UpdatePaymentLinkPaymentLinksResponseDocumentation(BaseModel):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str

    type: str


class UpdatePaymentLinkPaymentLinksResponseLinksTypedDict(TypedDict):
    documentation: UpdatePaymentLinkPaymentLinksResponseDocumentationTypedDict
    r"""The URL to the generic Mollie API error handling guide."""


class UpdatePaymentLinkPaymentLinksResponseLinks(BaseModel):
    documentation: UpdatePaymentLinkPaymentLinksResponseDocumentation
    r"""The URL to the generic Mollie API error handling guide."""


class UpdatePaymentLinkPaymentLinksResponseResponseBodyData(BaseModel):
    status: int
    r"""The status code of the error message. This is always the same code as the status code of the HTTP message itself."""

    title: str
    r"""The HTTP reason phrase of the error. For example, for a `404` error, the `title` will be `Not Found`."""

    detail: str
    r"""A detailed human-readable description of the error that occurred."""

    links: Annotated[
        UpdatePaymentLinkPaymentLinksResponseLinks, pydantic.Field(alias="_links")
    ]

    field: Optional[str] = None
    r"""If the error was caused by a value provided by you in a specific field, the `field` property will contain the name of the field that caused the issue."""


class UpdatePaymentLinkPaymentLinksResponseResponseBody(Exception):
    r"""An error response object."""

    data: UpdatePaymentLinkPaymentLinksResponseResponseBodyData

    def __init__(self, data: UpdatePaymentLinkPaymentLinksResponseResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, UpdatePaymentLinkPaymentLinksResponseResponseBodyData
        )


class UpdatePaymentLinkPaymentLinksDocumentationTypedDict(TypedDict):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str
    type: str


class UpdatePaymentLinkPaymentLinksDocumentation(BaseModel):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str

    type: str


class UpdatePaymentLinkPaymentLinksLinksTypedDict(TypedDict):
    documentation: UpdatePaymentLinkPaymentLinksDocumentationTypedDict
    r"""The URL to the generic Mollie API error handling guide."""


class UpdatePaymentLinkPaymentLinksLinks(BaseModel):
    documentation: UpdatePaymentLinkPaymentLinksDocumentation
    r"""The URL to the generic Mollie API error handling guide."""


class UpdatePaymentLinkPaymentLinksResponseBodyData(BaseModel):
    status: int
    r"""The status code of the error message. This is always the same code as the status code of the HTTP message itself."""

    title: str
    r"""The HTTP reason phrase of the error. For example, for a `404` error, the `title` will be `Not Found`."""

    detail: str
    r"""A detailed human-readable description of the error that occurred."""

    links: Annotated[UpdatePaymentLinkPaymentLinksLinks, pydantic.Field(alias="_links")]

    field: Optional[str] = None
    r"""If the error was caused by a value provided by you in a specific field, the `field` property will contain the name of the field that caused the issue."""


class UpdatePaymentLinkPaymentLinksResponseBody(Exception):
    r"""An error response object."""

    data: UpdatePaymentLinkPaymentLinksResponseBodyData

    def __init__(self, data: UpdatePaymentLinkPaymentLinksResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, UpdatePaymentLinkPaymentLinksResponseBodyData
        )


class UpdatePaymentLinkAmountTypedDict(TypedDict):
    r"""The amount of the payment link. If no amount is provided initially, the customer will be prompted to enter an amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkAmount(BaseModel):
    r"""The amount of the payment link. If no amount is provided initially, the customer will be prompted to enter an amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkPaymentLinksMinimumAmountTypedDict(TypedDict):
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkPaymentLinksMinimumAmount(BaseModel):
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkPaymentLinksAllowedMethods(str, Enum):
    APPLEPAY = "applepay"
    BANCOMATPAY = "bancomatpay"
    BANCONTACT = "bancontact"
    BANKTRANSFER = "banktransfer"
    BELFIUS = "belfius"
    BLIK = "blik"
    CREDITCARD = "creditcard"
    EPS = "eps"
    GIFTCARD = "giftcard"
    IDEAL = "ideal"
    KBC = "kbc"
    MYBANK = "mybank"
    PAYBYBANK = "paybybank"
    PAYPAL = "paypal"
    PAYSAFECARD = "paysafecard"
    POINTOFSALE = "pointofsale"
    PRZELEWY24 = "przelewy24"
    SATISPAY = "satispay"
    TRUSTLY = "trustly"
    TWINT = "twint"


class UpdatePaymentLinkPaymentLinksAmountTypedDict(TypedDict):
    r"""The fee that you wish to charge.

    Be careful to leave enough space for Mollie's own fees to be deducted as well. For example, you cannot charge a €0.99 fee on a €1.00 payment.
    """

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkPaymentLinksAmount(BaseModel):
    r"""The fee that you wish to charge.

    Be careful to leave enough space for Mollie's own fees to be deducted as well. For example, you cannot charge a €0.99 fee on a €1.00 payment.
    """

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class UpdatePaymentLinkApplicationFeeTypedDict(TypedDict):
    r"""With Mollie Connect you can charge fees on payment links that your app is processing on behalf of other Mollie merchants.

    If you use OAuth to create payment links on a connected merchant's account, you can charge a fee using this `applicationFee` parameter. If a payment on the payment link succeeds, the fee will be deducted from the merchant's balance and sent to your own account balance.
    """

    amount: NotRequired[UpdatePaymentLinkPaymentLinksAmountTypedDict]
    r"""The fee that you wish to charge.

    Be careful to leave enough space for Mollie's own fees to be deducted as well. For example, you cannot charge a €0.99 fee on a €1.00 payment.
    """
    description: NotRequired[str]
    r"""The description of the application fee. This will appear on settlement reports towards both you and the connected merchant."""


class UpdatePaymentLinkApplicationFee(BaseModel):
    r"""With Mollie Connect you can charge fees on payment links that your app is processing on behalf of other Mollie merchants.

    If you use OAuth to create payment links on a connected merchant's account, you can charge a fee using this `applicationFee` parameter. If a payment on the payment link succeeds, the fee will be deducted from the merchant's balance and sent to your own account balance.
    """

    amount: Optional[UpdatePaymentLinkPaymentLinksAmount] = None
    r"""The fee that you wish to charge.

    Be careful to leave enough space for Mollie's own fees to be deducted as well. For example, you cannot charge a €0.99 fee on a €1.00 payment.
    """

    description: Optional[str] = None
    r"""The description of the application fee. This will appear on settlement reports towards both you and the connected merchant."""


class UpdatePaymentLinkSelfTypedDict(TypedDict):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class UpdatePaymentLinkSelf(BaseModel):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class UpdatePaymentLinkPaymentLinkTypedDict(TypedDict):
    r"""The URL your customer should visit to make the payment. This is where you should redirect the customer to."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class UpdatePaymentLinkPaymentLink(BaseModel):
    r"""The URL your customer should visit to make the payment. This is where you should redirect the customer to."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class UpdatePaymentLinkDocumentationTypedDict(TypedDict):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class UpdatePaymentLinkDocumentation(BaseModel):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class UpdatePaymentLinkLinksTypedDict(TypedDict):
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    self_: NotRequired[UpdatePaymentLinkSelfTypedDict]
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""
    payment_link: NotRequired[UpdatePaymentLinkPaymentLinkTypedDict]
    r"""The URL your customer should visit to make the payment. This is where you should redirect the customer to."""
    documentation: NotRequired[UpdatePaymentLinkDocumentationTypedDict]
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""


class UpdatePaymentLinkLinks(BaseModel):
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    self_: Annotated[Optional[UpdatePaymentLinkSelf], pydantic.Field(alias="self")] = (
        None
    )
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    payment_link: Annotated[
        Optional[UpdatePaymentLinkPaymentLink], pydantic.Field(alias="paymentLink")
    ] = None
    r"""The URL your customer should visit to make the payment. This is where you should redirect the customer to."""

    documentation: Optional[UpdatePaymentLinkDocumentation] = None
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""


class UpdatePaymentLinkResponseBodyTypedDict(TypedDict):
    r"""The payment link object."""

    resource: NotRequired[str]
    r"""Indicates the response contains a payment link object. Will always contain the string `payment-link` for this endpoint."""
    id: NotRequired[str]
    r"""The identifier uniquely referring to this payment link. Example: `pl_4Y0eZitmBnQ6IDoMqZQKh`."""
    mode: NotRequired[str]
    r"""Whether this entity was created in live mode or in test mode.

    Possible values: `live` `test`
    """
    description: NotRequired[str]
    r"""A short description of the payment link. The description is visible in the Dashboard and will be shown on the customer's bank or card statement when possible."""
    amount: NotRequired[Nullable[UpdatePaymentLinkAmountTypedDict]]
    r"""The amount of the payment link. If no amount is provided initially, the customer will be prompted to enter an amount."""
    minimum_amount: NotRequired[
        Nullable[UpdatePaymentLinkPaymentLinksMinimumAmountTypedDict]
    ]
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""
    archived: NotRequired[bool]
    r"""Whether the payment link is archived. Customers will not be able to complete payments on archived payment links."""
    redirect_url: NotRequired[Nullable[str]]
    r"""The URL your customer will be redirected to after completing the payment process. If no redirect URL is provided, the customer will be shown a generic message after completing the payment."""
    webhook_url: NotRequired[Nullable[str]]
    r"""The webhook URL where we will send payment status updates to.

    The webhookUrl is optional, but without a webhook you will miss out on important status changes to any payments resulting from the payment link.

    The webhookUrl must be reachable from Mollie's point of view, so you cannot use `localhost`. If you want to use webhook during development on `localhost`, you must use a tool like ngrok to have the webhooks delivered to your local machine.
    """
    profile_id: NotRequired[Nullable[str]]
    r"""The identifier referring to the [profile](get-profile) this entity belongs to.

    Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted in the creation request. For organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.
    """
    reusable: NotRequired[Nullable[bool]]
    r"""Indicates whether the payment link is reusable. If this field is set to `true`, customers can make multiple payments using the same link.

    If no value is specified, the field defaults to `false`, allowing only a single payment per link.
    """
    created_at: NotRequired[str]
    r"""The entity's date and time of creation, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format."""
    paid_at: NotRequired[Nullable[str]]
    r"""The date and time the payment link became paid, in ISO 8601 format."""
    expires_at: NotRequired[Nullable[str]]
    r"""The date and time the payment link is set to expire, in ISO 8601 format. If no expiry date was provided up front, the payment link will not expire automatically."""
    allowed_methods: NotRequired[
        Nullable[List[UpdatePaymentLinkPaymentLinksAllowedMethods]]
    ]
    r"""An array of payment methods that are allowed to be used for this payment link. When this parameter is not provided or is an empty array, all enabled payment methods will be available."""
    application_fee: NotRequired[UpdatePaymentLinkApplicationFeeTypedDict]
    r"""With Mollie Connect you can charge fees on payment links that your app is processing on behalf of other Mollie merchants.

    If you use OAuth to create payment links on a connected merchant's account, you can charge a fee using this `applicationFee` parameter. If a payment on the payment link succeeds, the fee will be deducted from the merchant's balance and sent to your own account balance.
    """
    links: NotRequired[UpdatePaymentLinkLinksTypedDict]
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""


class UpdatePaymentLinkResponseBody(BaseModel):
    r"""The payment link object."""

    resource: Optional[str] = "payment-link"
    r"""Indicates the response contains a payment link object. Will always contain the string `payment-link` for this endpoint."""

    id: Optional[str] = None
    r"""The identifier uniquely referring to this payment link. Example: `pl_4Y0eZitmBnQ6IDoMqZQKh`."""

    mode: Optional[str] = None
    r"""Whether this entity was created in live mode or in test mode.

    Possible values: `live` `test`
    """

    description: Optional[str] = None
    r"""A short description of the payment link. The description is visible in the Dashboard and will be shown on the customer's bank or card statement when possible."""

    amount: OptionalNullable[UpdatePaymentLinkAmount] = UNSET
    r"""The amount of the payment link. If no amount is provided initially, the customer will be prompted to enter an amount."""

    minimum_amount: Annotated[
        OptionalNullable[UpdatePaymentLinkPaymentLinksMinimumAmount],
        pydantic.Field(alias="minimumAmount"),
    ] = UNSET
    r"""The minimum amount of the payment link. This property is only allowed when there is no amount provided. The customer will be prompted to enter a value greater than or equal to the minimum amount."""

    archived: Optional[bool] = None
    r"""Whether the payment link is archived. Customers will not be able to complete payments on archived payment links."""

    redirect_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="redirectUrl")
    ] = UNSET
    r"""The URL your customer will be redirected to after completing the payment process. If no redirect URL is provided, the customer will be shown a generic message after completing the payment."""

    webhook_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="webhookUrl")
    ] = UNSET
    r"""The webhook URL where we will send payment status updates to.

    The webhookUrl is optional, but without a webhook you will miss out on important status changes to any payments resulting from the payment link.

    The webhookUrl must be reachable from Mollie's point of view, so you cannot use `localhost`. If you want to use webhook during development on `localhost`, you must use a tool like ngrok to have the webhooks delivered to your local machine.
    """

    profile_id: Annotated[OptionalNullable[str], pydantic.Field(alias="profileId")] = (
        UNSET
    )
    r"""The identifier referring to the [profile](get-profile) this entity belongs to.

    Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted in the creation request. For organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.
    """

    reusable: OptionalNullable[bool] = False
    r"""Indicates whether the payment link is reusable. If this field is set to `true`, customers can make multiple payments using the same link.

    If no value is specified, the field defaults to `false`, allowing only a single payment per link.
    """

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None
    r"""The entity's date and time of creation, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format."""

    paid_at: Annotated[OptionalNullable[str], pydantic.Field(alias="paidAt")] = UNSET
    r"""The date and time the payment link became paid, in ISO 8601 format."""

    expires_at: Annotated[OptionalNullable[str], pydantic.Field(alias="expiresAt")] = (
        UNSET
    )
    r"""The date and time the payment link is set to expire, in ISO 8601 format. If no expiry date was provided up front, the payment link will not expire automatically."""

    allowed_methods: Annotated[
        OptionalNullable[List[UpdatePaymentLinkPaymentLinksAllowedMethods]],
        pydantic.Field(alias="allowedMethods"),
    ] = UNSET
    r"""An array of payment methods that are allowed to be used for this payment link. When this parameter is not provided or is an empty array, all enabled payment methods will be available."""

    application_fee: Annotated[
        Optional[UpdatePaymentLinkApplicationFee],
        pydantic.Field(alias="applicationFee"),
    ] = None
    r"""With Mollie Connect you can charge fees on payment links that your app is processing on behalf of other Mollie merchants.

    If you use OAuth to create payment links on a connected merchant's account, you can charge a fee using this `applicationFee` parameter. If a payment on the payment link succeeds, the fee will be deducted from the merchant's balance and sent to your own account balance.
    """

    links: Annotated[
        Optional[UpdatePaymentLinkLinks], pydantic.Field(alias="_links")
    ] = None
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "resource",
            "id",
            "mode",
            "description",
            "amount",
            "minimumAmount",
            "archived",
            "redirectUrl",
            "webhookUrl",
            "profileId",
            "reusable",
            "createdAt",
            "paidAt",
            "expiresAt",
            "allowedMethods",
            "applicationFee",
            "_links",
        ]
        nullable_fields = [
            "amount",
            "minimumAmount",
            "redirectUrl",
            "webhookUrl",
            "profileId",
            "reusable",
            "paidAt",
            "expiresAt",
            "allowedMethods",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
