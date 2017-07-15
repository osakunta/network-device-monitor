import requests, json
from data.data import slack_channel

# Uses 'requests' library to send a http POST request to 'webhook_url' with a body 'message'
def send_slack_notification(webhook_url, message):
    headers = {'Content-type': 'application/json'}
    request = requests.post(webhook_url, headers=headers, data=json.dumps(message))

    print(request.status_code)
    print(request.content)

# Return a dictionary which represents JSON body of the Slack notification POST request
# Documentation can be found here: https://api.slack.com/docs/messages
def slack_message(host):
     return {
        "channel": slack_channel,
        "username": "Network Device Monitor",
        "icon_emoji": ":warning:",
        "attachments": [
            {
                "fallback": "Host at " + host[1] + " does not respond.",
                "color": "warning",
                "author_name": host[1],
                "author_link": slack_host_url(host),
                "title": host[0],
                "text": "The host does not respond to requests."
            }
        ]
    }

# Returns URL with port if it is defined, otherwize without
def slack_host_url(host):
    return "http://" + host[1] + (":" + host[2] if len(host) == 3 else "")
