#!/bin/bash python
import requests
import datetime
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("--user", help="insert github username")
arg.add_argument("--repo", help="insert gthub repository")
arg.add_argument("--pull", help="insert number of github pull-request")
arg.add_argument("--login", help="insert github login")
arg.add_argument("--token", help="insert github token")
arg.add_argument("--version", action='version', version='%(prog)s 1.0')

arg.add_argument('--all', help="output all available parameters", action="store_true")
arg.add_argument('-du', help='output date of updated pull request', action="store_true")
arg.add_argument('-dc', help='output day of created pull request', action="store_true")
arg.add_argument('-il', help='output number of inserted line(s)', action="store_true")
arg.add_argument('-dl', help='output number of delete line(s)', action="store_true")
arg.add_argument('-cr', help='output creator pull request', action="store_true")
arg.add_argument('-dfc', help='output number of day after created request', action="store_true")

arg = arg.parse_args()

token = login = ''

if arg.login is not None:
    login = arg.login

if arg.token is not None:
    token = arg.token

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

if arg.all or arg.du:
    print("date of updated ", update)
if arg.all or arg.dc:
    print("day of created: ", create[8:10])
if arg.all or arg.il:
    print("inserted line(s): ", addline)
if arg.all or arg.dl:
    print("deleted line(s): ", deliteline)
if arg.all or arg.cr:
    print("creator: ", usercreated)
if arg.all or arg.dfc:
    print("number of day after created: ", daysopened.days)
