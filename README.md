Network Device Monitor
======================

This is a simple script implemented in `Python 3` which pings host devices and sends a Slack notification if the device does not respond.

Setup
-----
In `data` directory copy the `data.py.sample` file as `data.py`.
```
cp data/data.py.sample data/data.py
```
Set the variables as instructed in the comments. You need a Slack channel with an `Incoming Webhooks` integration installed on that channel.

Restrictions
------------
This script will only work with hosts which allow ping.
