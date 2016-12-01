#!/usr/bin/env python3
import subprocess

output = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE).stdout

if len(output) == 0:
    sys.exit(0)
else:
    sys.exit(1)
