import os
import json
import requests


des_username = input("Enter your destination username: ")
des_password = input("Enter your destination token: ")
REPO_OWNER = input("Enter your destination repo owner: ")
REPO_NAME = input("Enter your destination repo name: ")
source_username = input("Enter your source username: ")
source_password = input("Enter your source token: ")

def get_labels():
    session = requests.Session()
    session.auth = (source_username, source_password)
    labels = requests.get('https://ec2-34-213-47-149.us-west-2.compute.amazonaws.com/api/v3/repos/capgemini/test/labels', auth=session.auth, verify=False)
    return labels

#y = get_labels()
#print(y.json())

def create_github_label(label):
    url = 'https://api.github.com/repos/%s/%s/labels' % (REPO_OWNER, REPO_NAME)
    session = requests.Session()
    session.auth = (des_username, des_password)
    labels = {'name': label[0]['name']}
    r = session.post(url, json.dumps(labels))
    if r.status_code == 201:
        print ('Successfully created labels')
    else:
        print ('Could not create labels' + str(r.content) )

y = get_labels()
#print(y.json())
create_github_label(y.json())
