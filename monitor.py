from sample.ping import ping as responds
from sample.slack import *
from data.data import *

# Loops through all hosts from data.py and sends a Slack notification
# every time a host does not respond
for host in hosts:
    if not responds(host[1]):
        send_slack_notification(slack_webhook_url, slack_message(host))
