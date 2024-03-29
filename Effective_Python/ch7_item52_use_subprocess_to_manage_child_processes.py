# Chapter 7: Concurrency and Parallelism

# Concurrency enables a computer to do many different things seemingly at the same time.
    # Concurrency providing the illusion that the program are running simultaneously
    # Within a single program, concurrency is a tool that makes it easier for programmers to solve
    # certain types of problems.
    # concurrent programs enable many distinct paths of execution, including separate streams of I/O
    # To make forward progress in a way that seem to be both simultaneous and independent.

# Parallelism, in contrast, involves actually doing many different things at the same time.
    # multiple CPU Cores can execute multiple programs simultaneously.


# Key difference between Parallelism and Concurrency:
    # Speedup
        # two distinct paths of execution in a program make forward progress in parallel
        # the time it takes to do the total work is cut in half.
        # concurrent programs may run thousands of separate paths of execution seemingly
        # in parallel but provide no speedup for the total work.


# How Python support Concurrency?
    # threads
    # coroutines: enable vast numbers of concurrent functions

# How python support Parallel?
    # system calls
    # subprocesses
    # C extensions

# The thing is:
    # it can be very difficult to make concurrent python code truly run in parallel.

# Python provide battle-hardened libraries for running and managing child processes.
    # built-in module: subprocess


# Example: use the subprocess run convenience function to start a process, read its output,
# and verify that it terminated cleanly

import subprocess

result = subprocess.run(
    ['echo', "Hello spring! "],
    capture_output=True,
    encoding='utf-8')

result.check_returncode()
print(result.stdout)


# what is supprocess's parent process?
    # the python interpreter

# Example: use subprocess.Popen class and poll child process status periodically while python does other work.

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('python working...')
print('Exist status', proc.poll())

# Example: Decoupling the child process from the parent frees up the parent process to run many child processes
# in parallel
# starting all the child processes together with Popen unfront.

import time

start = time.time()
sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'])
    sleep_procs.append(proc)


# wait for all the child processes to finish their I/O and terminate with the communicate method.
for proc in sleep_procs:
    proc.communicate()

end = time.time()
delta = end - start
print(f'Finished in {delta:.3} seconds')


# pipe data from a python program into a subprocess and retrieve its output
# this allows you to utilize many other programs to do work in parallel

# For example:
# I want to use the openssl command-line tool to encrypt some data.
# starting the child process with command-line arguments and I/O pipes.

import os

def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'jdkf;asdkdfjsa'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)

    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    procs.append(proc)

# wait all the child processes to finish and then retrieve their final output

for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])


# create chains of parallel processes, just like unix pipelines
# connecting the output of one child process to the input of another.

# starts the openssl cmd-line tool as a subprocess to generate a whirlpool has of the input stream:

def run_hash(input_stdin):
    return subprocess.Popen(
        ['openssl', 'dgst', '-whirlpool', '-binary'],
        stdin=input_stdin,
        stdout=subprocess.PIPE)


encrypt_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(100)

    encrypt_proc = run_encrypt(data)
    encrypt_procs.append(encrypt_proc)

    hash_proc = run_hash(encrypt_proc.stdout)
    hash_procs.append(hash_proc)

    encrypt_proc.stdout.close()
    encrypt_proc.stdout = None

for proc in encrypt_procs:
    proc.communicate()
    assert proc.returncode == 0

for proc in hash_procs:
    out, _ = proc.communicate()
    print(out[-10:])
    assert proc.returncode == 0

# what happend if one subprocess hanged, waiting forever?
# pass the timeout parameter to the communicate method.
# give the chance to terminate the misbehaving subprocesses.

proc = subprocess.Popen(['sleep', '10'])
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()
print('Exit status', proc.poll())

# Things-to-Remember:
# 1. Use the subprocess module to run child processes and manage their input and output streams.
# 2. child processes run in parallel with the python interpreter, enabling you to maximize your usage of CPU cores.
# 3. Use the run convenience function for simple usage, and the Popen class for advanced usage like Unix-style pipelines
# 4. use the timeout parameter of the communicate method to avoid deadlocks and haning child processes.
