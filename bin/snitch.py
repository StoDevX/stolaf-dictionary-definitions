#!/usr/bin/env python3
import sys
import requests

if len(sys.argv) < 3:
    print('usage: snitch.py <msg>')
    sys.exit(1)

requests.post('https://nosnch.in/abf7027315', data={'m': sys.argv[2]})
