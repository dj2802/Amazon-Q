import json

def lambda_handler(event, context):
    """Approves valid invoice"""
    invoice = event.get('invoice', {})
    
    return {
        'statusCode': 200,
        'status': 'approved',
        'invoice': invoice,
        'approvalId': f"APP-{context.aws_request_id[:8]}",
        'message': 'Invoice approved successfully'
    }