#!python3

import git
import inquirer
import requests
import signal
import sys

version = 3

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  END = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

scriptFile = requests.get('https://raw.githubusercontent.com/mbrammer/git-trailer-prompt/main/commit.py')

for line in scriptFile.text.splitlines():
  version_line = line.split(' = ')

  if "version =" in line and version_line[0] == 'version' and int(version_line[1]) < version:
    print(bcolors.HEADER)
    print('======================================================================================')
    print(' A newer version of git-trailer-prompt is available.')
    print(' Go to https://github.com/mbrammer/git-trailer-prompt and install the latest version.')
    print('======================================================================================')
    print(bcolors.END)

def handler(signum, frame):
  sys.exit('Nothing committed! Bye!')
 
signal.signal(signal.SIGINT, handler)

try:
  repo = git.Repo('.')
except:
  sys.exit('This directory is not a git repository.')

if not repo.is_dirty(untracked_files=True):
  sys.exit('You have no changes in the repository.')

if len(repo.index.diff("HEAD")) == 0:
  sys.exit('There is nothing to commit.')
  # repo.git.add('--all')

questions_provide_changelog = [
  inquirer.Confirm("changelog", message="Do you want to create a changelog message"),
]

answers_provide_changelog = inquirer.prompt(questions_provide_changelog)

if answers_provide_changelog['changelog']:
  questions_changelog = [
    inquirer.List('trailer',
        message="Please select a changelog type ans press enter",
        choices=[
          'added: New feature',
          'fixed: Bug fix',
          'changed: Feature change',
          'deprecated: New deprecation',
          'removed: Feature removal',
          'security: Security fix',
          'performance: Performance improvement',
          'other: Other',
        ],
    ),
    inquirer.Text('message', message='Please provide a non-technical changelog message'),
  ]

  answers_changelog = inquirer.prompt(questions_changelog)

  trailer = answers_changelog["trailer"].split(':')

  repo.git.commit('-m', answers_changelog["message"], trailer=f'Changelog: {trailer[0]}')
else:
  questions_commit = [
    inquirer.Text('message', message='Please provide a commit message'),
  ]

  answers_commit = inquirer.prompt(questions_commit)

  repo.git.commit('-m', answers_commit["message"])
