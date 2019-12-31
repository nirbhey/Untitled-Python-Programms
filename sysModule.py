"""

You can communicate back with the shel from the script, by opening cmd and typing;

import subprocess

subprocess.call('python sysModule.py "arguments"', shell = True)

# To store the output you can type;

varOutput = subprocess.check_output('python sysModule.py "arguments"', shell = True)
print(varOutput)

"""
import sys

def main(var1):
    print('From main',var1)

sys.stderr.write("This is an error text!\n")

sys.stderr.flush()

sys.stdout.write("This is the system.out.print of python!\n")

print(sys.argv) # Use this to communicate b/w python and other language. This is used to send commandline arguments.

if len(sys.argv) > 1:
    print(sys.argv[1])
    print(float(sys.argv[1]) + 5)

main(sys.argv[1])

