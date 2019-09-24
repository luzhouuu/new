import requests
import json

def requestGoTag(body, tagid):
    # if tagid > 3:
    #     return print('exceed max tagid ')
    url = "http://localhost:1333/user_story/similar"

    payload =  "{\n\t\"body\": \"" + body + "\",\n\t\"tagId\":" + str(tagid) + "\n}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.16.3",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "87922156-f986-4392-a503-97ba7330019c,b92142c8-b022-4f48-aae4-fb68d93ec554",
        'Host': "localhost:1333",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "37",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    capability = result[0]['capability']
    subcapability = result[0]['subcapability']
    epic = result[0]['epic']
    return capability, subcapability, epic
