
# Adding comment for new commit
# Adding comment for new commit


def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'body': "test response body",
        'headers': {
            "Content-Type": "application/json"
        }
    }