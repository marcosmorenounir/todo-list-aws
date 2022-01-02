import json


def translate(event, context):
    # create a response
    #item = todoList.get_item(event['pathParameters']['id'])
    print(event)
    """
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    """
    return {
            "statusCode": 404,
            "body": ""
        }
