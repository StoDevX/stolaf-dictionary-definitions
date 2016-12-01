#!/bin/bash -ev

rm -rf repo
git clone https://github.com/StoDevX/stolaf-dictionary-definitions.git repo
cd repo

python3 bin/check.py

if ! [[ -n "$(git status --porcelain)" ]]; then
  curl -d "m=no changes" https://nosnch.in/abf7027315
  exit 0
fi

git checkout master
DATE=$(date "+%Y-%m-%d_%H-%M-%S")
BRANCH="new-data_$DATE"
git checkout -b "$BRANCH"

MSG="data update for $(date)"
git add -- *.html
git commit -m "$MSG"
git commit --amend --author "Dictionary Bot <hawkrives+stolaf-dictionary-bot@gmail.com>" --no-edit

git push origin "$BRANCH"

TITLE="$MSG"
HEAD="$BRANCH"
BASE="master"
DATA="{\"title\":\"$TITLE\",\"head\":\"$HEAD\",\"base\":\"$BASE\"}"

CONTENT_TYPE="Content-Type: application/json"
ACCEPT="Accept: application/vnd.github.v3+json"

URL="https://api.github.com/repos/StoDevX/stolaf-dictionary-definitions/pulls"

curl -u "hawkrives:$GH_KEY" -H "$CONTENT_TYPE" -H "$ACCEPT" -d "$DATA" "$URL"

curl -d "m=changes happened" https://nosnch.in/abf7027315
