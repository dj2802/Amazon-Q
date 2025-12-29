def lambda_handler(event, context):
    invoice_id = event.get("invoiceId")
    amount = event.get("amount")
    vendor = event.get("vendor")

    return {
        "status": "APPROVED",
        "invoiceId": invoice_id,
        "amount": amount,
        "vendor": vendor
    }
