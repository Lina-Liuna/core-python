# The subprocess module allows you to spawn new processes,
# connect to their input/output/error pipes, and obtain their return codes.
import subprocess
import os

subprocess.run(["ls", "-l"])

subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
subprocess.run(["ls", "-l", "/dev/null"])
subprocess.Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])
subprocess.Popen(["/usr/bin/git","push"])

# use subprocess.run to push on github automatically.

# subprocess.run(['git', 'add',os.path.basename(__file__)])
# subprocess.run(['git', 'commit', '-m', 'commit a github by using subprocess run'])
# subprocess.run(['git', 'push'])


# Get the output of executing cmd in a shell
print(subprocess.getstatusoutput('ls -l'))
print(subprocess.getoutput('ls -l'))
