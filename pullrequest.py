import os
import json
import requests


des_username = input("Enter your destination username: ")
des_password = input("Enter your destination token: ")
REPO_OWNER = input("Enter your destination repo owner: ")
REPO_NAME = input("Enter your destination repo name: ")
source_username = input("Enter your source username: ")
source_password = input("Enter your source token: ")

def get_pullRequests():
    session = requests.Session()
    session.auth = (source_username, source_password)
    pullRequest = requests.get('https://ec2-34-213-47-149.us-west-2.compute.amazonaws.com/api/v3/repos/capgemini/test/pulls', auth=session.auth, verify=False)
    #print(x.json())
    return pullRequest

#y = get_pullRequests()
#print(y.json())

def create_github_pullRequests( js):  
    url = 'https://api.github.com/repos/%s/%s/pulls' % (REPO_OWNER, REPO_NAME)
    session = requests.Session()
    session.auth = (des_username, des_password)
    issue = {'title': js[0]['title']
             }
    r = session.post(url, json.dumps(issue))
    #r = session.post(url, js[0])
    #print(js[0]['title'])
   # print(issue['title'])
    if r.status_code == 201:
        print ('Successfully created pullrequests')
    else:
        print ('Could not create pullrequests' + str(r.content) )

y = get_pullRequests()
#print(y.json())
create_github_pullRequests(y.json())
