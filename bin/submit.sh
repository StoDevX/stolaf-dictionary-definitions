#!/bin/bash
set -ve

if ! [[ -n "$(git status --porcelain)" ]]; then
  bin/snitch.py "no changes"
else
  bin/submit-pr.py
  bin/snitch.py "changes happened"
fi
