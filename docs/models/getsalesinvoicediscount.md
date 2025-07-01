# GetSalesInvoiceDiscount

The discount to be applied to the entire invoice, applied on top of any line item discounts.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `type`                                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | The type of discount.<br/><br/>Possible values: `amount` `percentage`                  | amount                                                                                 |
| `value`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | A string containing an exact monetary amount in the given currency, or the percentage. | 10.00                                                                                  |