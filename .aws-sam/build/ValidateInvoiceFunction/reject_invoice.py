import json

def lambda_handler(event, context):
    """Rejects invalid invoice"""
    invoice = event.get('invoice', {})
    
    return {
        'statusCode': 200,
        'status': 'rejected',
        'invoice': invoice,
        'rejectionId': f"REJ-{context.aws_request_id[:8]}",
        'message': 'Invoice rejected due to validation failure'
    }