# ListMethodsResponseBody

A list of payment method objects. For a complete reference of the payment method object, refer to the [Get payment method endpoint](get-method) documentation.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `count`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | The number of payment method objects in this result set. Results are **not** paginated. |
| `embedded`                                                                              | [Optional[models.ListMethodsEmbedded]](../models/listmethodsembedded.md)                | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `links`                                                                                 | [Optional[models.ListMethodsLinks]](../models/listmethodslinks.md)                      | :heavy_minus_sign:                                                                      | N/A                                                                                     |