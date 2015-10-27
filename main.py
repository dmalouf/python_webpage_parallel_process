#!/usr/bin/python3

import subprocess
import os

pythonFileToRun = "backgroundTask.py"

# Without this, anything that goes to the browser will just throw a 500
print("Content-type: text/html\r\n\r\n")

# Gather data from <form>, query-string, etc. for passing along via CLI
# - VITAL that these are sanitized!
someArgs = "something here"

# Setup the executable
the_executable = str("{}/" + j.format(os.getcwd()))
args = ['/usr/bin/python3', the_executable, someArg]

# Start sub-process
sts = subprocess.Popen(args)
