#!/usr/bin/env python3
from subprocess import run, PIPE
from datetime import datetime
import os

date = datetime.now().isoformat()

run(['git', 'checkout', 'master'])
branch = "new-data_" + date
run(['git', 'checkout', '-b', branch])

author = "Dictionary Bot <hawkrives+stolaf-dictionary-bot@gmail.com>"
msg = "data update for " + date
run(['git', 'add', '--', '*.html'])
run(['git', 'commit', '-m', msg])
run(['git', 'commit', '--amend', '--author', author, '--no-edit'])

run(['git', 'push', 'origin', branch])

# # # # #

url = "https://api.github.com/repos/StoDevX/stolaf-dictionary-definitions/pulls"
auth = ('hawkrives', os.getenv('GH_KEY'))
data = {'title': msg, 'head': branch, 'base': 'master'}
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.github.v3+json",
}

requests.post(url, data=data, headers=headers, auth=auth)
