import requests, json
from data.data import slack_channel

headers = {'Content-type': 'application/json'}

def send_slack_notification(webhook_url, message):
    r = requests.post(webhook_url, headers=headers, data=json.dumps(message))
    print(r.status_code)
    print(r.content)

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
