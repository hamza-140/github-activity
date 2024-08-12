import requests
import sys
if len(sys.argv) != 2:
    print("Usage: python github-activity.py <username>")
    sys.exit(1)
response = requests.get(f'https://api.github.com/users/{sys.argv[1]}/events')
PushEvent = {}
CreateEvent = {}
PullRequestEvent = {}
IssuesEvents = {}
IssueCommentEvents = {}
ForkEvents = {}
StarEvents = {}
WatchEvents = {}
ReleaseEvents = {}
DeploymentEvents = {}
RepositoryEvents = {}
events = [
    {'type': 'PushEvent', 'data': PushEvent},
    {'type': 'CreateEvent', 'data': CreateEvent},
    {'type': 'PullRequestEvent', 'data': PullRequestEvent},
    {'type': 'IssuesEvents', 'data': IssuesEvents},
    {'type': 'IssueCommentEvents', 'data': IssueCommentEvents},
    {'type': 'ForkEvents', 'data': ForkEvents},
    {'type': 'StarEvents', 'data': StarEvents},
    {'type': 'WatchEvents', 'data': WatchEvents},
    {'type': 'ReleaseEvents', 'data': ReleaseEvents},
    {'type': 'DeploymentEvents', 'data': DeploymentEvents},
    {'type': 'RepositoryEvents', 'data': RepositoryEvents}
]
if response.status_code==200:
    data = response.json()
    for i in range(0,len(data)):
        for e in events:
            if(data[i]['type']==str(e['type'])):
                if(data[i]['repo']['name'] in e['data']):
                    e['data'][data[i]['repo']['name']]+=1
                else:
                    e['data'][data[i]['repo']['name']]=1
    def display(type,dict):
        for k,i in dict.items():
            print(f"- {type} {i} commits in {k}")

    for d in events:
        display(str(d['type']).replace('Event',''),d['data'])
else:
    print("Error retrieving Github data!")