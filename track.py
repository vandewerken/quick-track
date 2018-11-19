import json
from botocore.vendored import requests
import boto3 

def lambda_handler(event, context):

    # Set user-specific variables 
    feedId = open('FEED_ID.txt', 'r').read()
    shortened = open('static_shortened.txt', 'r').read()    # if you're sending out texts, you can either set the URL here or in another doc
    secretARN = open('arn.txt', 'r').read()

    spotMain = 'https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/'
    spotCall = '/latest.json'   # latest.json grabs the last message transmitted by SPOT
                                # message.json grabs the last set of messages and can be bounded using message.xml?=start
                                # more calls can be accessed here: https://faq.findmespot.com/index.php?action=showEntry&data=69

    spotUrl = (spotMain + feedId + spotCall)
    r = requests.get(spotMain + feedId + spotCall)
    response = r.json()

    spotLat = response['response']['feedMessageResponse']['messages']['message']['latitude']
    spotLong = response['response']['feedMessageResponse']['messages']['message']['longitude']
    messageId = response['response']['feedMessageResponse']['messages']['message']['id']
    batteryCondition = response['response']['feedMessageResponse']['messages']['message']['batteryState']

    if r.status_code == 200:
        goodResponse = "The tracker is on. The battery is %s. The boat can be found at %s, %s. To see on a map, click here: %s" % (batteryCondition, spotLat, spotLong, shortened)
        client = boto3.client('sns')
        responseSNS = client.publish(
            TargetArn = secretARN,
            Message = goodResponse
        )
    else:
        badResponse = "The tracker is not on and / or is not sending messages."
        client = boto3.client('sns')
        responseSNS = client.publish(
            TargetArn = secretARN,
            Message = badResponse
        )