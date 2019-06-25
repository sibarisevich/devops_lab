#!/bin/bash python
import requests
import datetime
import argparse

arg= argparse.ArgumentParser()
arg.add_argument("--user", help="insert github username")
arg.add_argument("--repo", help="insert gthub repository")
arg.add_argument("--pull", help="insert number of github pull-request")
arg.add_argument("--version", help="output version the app")

arg = arg.parse_args()

token = '5bab07c808f13d15751256338fccfa3a1332e8b7'
login = 'sibarisevich'

if arg.user == None:
    accaunt = 'alenaPy'
else:
    accaunt = arg.user

if arg.repo == None:
    repo = 'devops_lab'
else:
    repo = arg.repo 

if arg.pull == None:
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
create= m['created_at']
addline = m['additions']
usercreated = m['user']['login']
deliteline = m['deletions']
d1 = datetime.datetime.strptime(create, "%Y-%m-%dT%H:%M:%SZ")
daysopened = datetime.datetime.now() - d1

print(" data obnovleniya: ", update, "\n", \
	"den sozdaniya: ", create[8:10], "\n", \
	"dobavleno strok: ", addline, "\n", \
	"udaleno strok: ", deliteline, "\n", \
	"sozdatel: ", usercreated, "\n", \
	"dney s sozdaniya: ", daysopened.days)
