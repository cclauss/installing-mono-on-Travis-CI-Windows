#!/usr/bin/env python

import os
from subprocess import check_call

path0 = set(os.getenv("PATH").split(";"))
check_call("choco install mono ; echo %PATH%".split(), shell=True)
path1 = set(os.getenv("PATH").split(";"))
print("\n".join(sorted(path1)))
print("sd:", path0 ^ path1)
