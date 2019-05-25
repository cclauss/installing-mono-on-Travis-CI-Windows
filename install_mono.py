#!/usr/bin/env python

import os
from subprocess import check_call

path0 = set(os.getenv("PATH").split(";"))
check_call("choco install mono".split())
path1 = set(os.getenv("PATH").split(";"))
print(path1)
