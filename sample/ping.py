from platform import system as system_name
from os import system as system_call

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request
    even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower() == "windows" else "-c 1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0
