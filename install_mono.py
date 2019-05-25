#!/usr/bin/env python3

import os
from subprocess import run

path0 = set(os.getenv("PATH").split(";"))
run("choco install mono".split())
path1 = set(os.getenv("PATH").split(";"))
print(path1)
