from urllib import request
from urllib.error import URLError, HTTPError
import json
import sys
import enum

class Event(enum.Enum):
    PushEvent = "Pushed"
    CreateEvent = "Created"
    PullRequestEvent = "Pulled"
    IssueCommentEvent = "Commented"
    ForkEvent = "Forked"

def formatter(result):

    for key, values in result.items():
        if key == Event.PushEvent.name:
            for kv, vv in values.items():
                print(f"{Event.PushEvent.value} {vv} commits to {kv}")
                break
        if key == Event.CreateEvent.name:
            for kv, vv in values.items():
                print(f"{Event.CreateEvent.value} {vv} events to {kv}")
                break
        if key == Event.PullRequestEvent.name:
            for kv, vv in values.items():
                print(f"{Event.PullRequestEvent.value} {vv} to {kv}")
                break
        if key == Event.IssueCommentEvent.name:
            for kv, vv in values.items():
                print(f"{Event.IssueCommentEvent.value} {vv} issues to {kv}")
                break
        if key == Event.ForkEvent.name:
            for kv, vv in values.items():
                print(f"{Event.ForkEvent.value} {vv} to {kv}")
                break
        #GENERIC
        for kv, vv in values.items():
                print(f"{key} {vv} to {kv}")
                break


def make_request(url):

    try:
        with request.urlopen(url) as response:
            data = response.read()
        response = json.loads(data)
        
        result = {}

        for item in response:
            item_type = item["type"]
            repo_name = item["repo"]["name"]

            if item_type not in result:
                result[item_type] = {}

            if repo_name not in result[item_type]:
                result[item_type][repo_name] = 0

            result[item_type][repo_name] += 1

        formatter(result)

    except HTTPError as e:
        print(f'Request Error: {e.code} - {e.reason}')
    except URLError as e:
        print(f'Conection Error: {e.reason}') 


if __name__ == "__main__":    
    
    if len(sys.argv) > 2:
        raise Exception("You pass more than 1 argument.")
    
    url = f"https://api.github.com/users/{sys.argv[1]}/events"
    
    make_request(url)      
