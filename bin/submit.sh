#!/bin/bash
set -ve

if ! [[ -n "$(git status --porcelain)" ]]; then
  ./snitch.py "no changes"
else
  ./submit-pr.py
  ./snitch.py "changes happened"
fi
