#!/usr/bin/env python3
from subprocess import run, PIPE
from datetime import datetime
import os
import requests

date = datetime.now().isoformat()

run(['git', 'checkout', 'master'], check=True)
branch = "new-data_" + date.replace(':', '-')
run(['git', 'checkout', '-b', branch], check=True)

author = "Dictionary Bot <hawkrives+stolaf-dictionary-bot@gmail.com>"
msg = "data update for " + date
run(['git', 'add', '--', '*.html'], check=True)
run(['git', 'commit', '-m', msg], check=True)
run(['git', 'commit', '--amend', '--author', author, '--no-edit'], check=True)

run(['git', 'push', 'origin', branch], check=True)

# # # # #

url = "https://api.github.com/repos/StoDevX/stolaf-dictionary-definitions/pulls"
auth = ('hawkrives', os.getenv('GH_KEY'))
data = {'title': msg, 'head': branch, 'base': 'master'}
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.github.v3+json",
}

requests.post(url, data=data, headers=headers, auth=auth)
