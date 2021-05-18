import os
import json
import requests
from get_issues import *


des_username = input("Enter your destination username: ")
des_password = input("Enter your destination token: ")
DES_REPO_OWNER = input("Enter your destination repo owner: ")
DES_REPO_NAME = input("Enter your destination repo name: ")
source_username = input("Enter your source username: ")
source_password = input("Enter your source token: ")
des_url = input("Enter your source url: ")

def get_issues():
    session = requests.Session()
    session.auth = (source_username, source_password)
    issue = requests.get(des_url, auth=session.auth, verify=False)
    #print(x.json())
    return issue

#y = get_issues()
#print(y.json())

def create_github_issue( js):  
    url = 'https://api.github.com/repos/%s/%s/issues' % (DES_REPO_OWNER, DES_REPO_NAME)
    session = requests.Session()
    session.auth = (des_username, des_password)
    issue = {'title': js[0]['title'],
             'body': js[0]['body'],
             'labels': js[0]['labels'],
             'created_at': js[0]['created_at']}
    r = session.post(url, json.dumps(issue))
    #r = session.post(url, js[0])
    #print(js[0]['title'])
    #print(issue['title'])
    if r.status_code == 201:
        print ('Successfully created Issue')
    else:
        print ('Could not create Issue' + str(r.content) )



y = get_issues()
#print(y.json())
create_github_issue(y.json())
