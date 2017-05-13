# _*_ coding: utf-8 _*_


def lambda_handler(event, context):
    return event


if __name__ == "__main__":
    event = {
        'key': 'value',
    }
    r = lambda_handler(event, {})
    print(r)
