import subprocess
import os
import datetime
import schedule
import time


file = os.getcwd()


def log_msg(file=os.path.basename(__file__), message="auto-sumbit-message:", when=None):
    if when is None:
        when = datetime.datetime.now()
    with open(file, 'w') as f:
        f.write(f'{when}: {message}')
    print(f'{when}: {message}')

def git_submit(file=os.path.basename(__file__)):
    log_msg(file)
    subprocess.run(['git', 'add', file])
    subprocess.run(['git', 'commit', '-m', 'automatically commit a github by using subprocess run'])
    subprocess.run(['git', 'push'])

def auto_submit(file=os.path.basename(__file__)):
    #schedule.every().day.at("01:00").do(git_submit, 'It is 01:00')o
    schedule.every(0.2).minutes.do(git_submit, 'It is 01:00')

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)

auto_submit()
