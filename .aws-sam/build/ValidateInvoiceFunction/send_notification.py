import json
import boto3

def lambda_handler(event, context):
    """Sends notification about invoice status"""
    status = event.get('status', 'unknown')
    invoice = event.get('invoice', {})
    
    # In real implementation, send SNS/SES notification
    notification_message = f"Invoice {invoice.get('id', 'N/A')} has been {status}"
    
    return {
        'statusCode': 200,
        'notificationSent': True,
        'message': notification_message,
        'status': status
    }