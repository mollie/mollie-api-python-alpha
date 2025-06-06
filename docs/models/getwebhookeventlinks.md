# GetWebhookEventLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.GetWebhookEventSelf]](../models/getwebhookeventself.md)                   | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `documentation`                                                                            | [Optional[models.GetWebhookEventDocumentation]](../models/getwebhookeventdocumentation.md) | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `entity`                                                                                   | [Optional[models.GetWebhookEventEntity]](../models/getwebhookevententity.md)               | :heavy_minus_sign:                                                                         | The API resource URL of the entity that this event belongs to.                             |