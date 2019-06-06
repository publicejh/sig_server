import requests
import json
from django.conf import settings


def get_user_detail(pk):
    headers = {
        'Content-Type': 'application/json', 'Accept': 'application/json',
        'Authorization': 'Api-Key ' + settings.AUTH_SERVER_API_KEY
    }
    res = requests.get(settings.AUTH_SERVER_GET_USER_API_URL + '/' + str(pk), headers=headers)

    if res.status_code != 200:
        return None

    return json.loads(res.content)
