#!/bin/bash python
import requests
import datetime
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("--user", help="insert github username")
arg.add_argument("--repo", help="insert gthub repository")
arg.add_argument("--pull", help="insert number of github pull-request")
arg.add_argument("--version", help="output version the app")

arg = arg.parse_args()

token = 'ba1dd0090b23c0b96d161a424fc8da24caa058d5'
login = 'sibarisevich'

if arg.user is None:
    accaunt = 'alenaPy'
else:
    accaunt = arg.user

if arg.repo is None:
    repo = 'devops_lab'
else:
    repo = arg.repo

if arg.pull is None:
    numberpull = '62'
else:
    numberpull = arg.pull

if arg.version:
    print("version 1.0")
    quit()

link = "https://api.github.com/repos/" + accaunt + "/" + repo + "/pulls/" + numberpull
r = requests.get(link, auth=(login, token))

m = r.json()
update = m['updated_at']
create = m['created_at']
addline = m['additions']
usercreated = m['user']['login']
deliteline = m['deletions']
d1 = datetime.datetime.strptime(create, "%Y-%m-%dT%H:%M:%SZ")
daysopened = datetime.datetime.now() - d1

print(" data obnovleniya: ", update)
print("den sozdaniya: ", create[8:10])
print("dobavleno strok: ", addline)
print("udaleno strok: ", deliteline)
print("sozdatel: ", usercreated)
print("dney s sozdaniya: ", daysopened.days)
