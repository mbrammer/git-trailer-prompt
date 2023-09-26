#!python3

import git
import os
import inquirer
import requests
from rich.console import Console
import signal
import sys
import argparse

version = 6

parser = argparse.ArgumentParser(description=f'git-trailer-prompt (v{version})')
parser.add_argument("-v", "--version", action='version', version=f'v{version}')
parser.add_argument("--update", action='store_true', help='Download and install the latest version')

args = parser.parse_args()

console = Console()

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

if args.update:
  console.print("[bold yellow]Updating git-trailer-prompt...")
  os.system("git clone git@github.com:mbrammer/git-trailer-prompt.git && cd git-trailer-prompt && sh ./setup.sh")
  console.print("[bold yellow]Update completed!")
  sys.exit()

scriptFile = requests.get('https://raw.githubusercontent.com/mbrammer/git-trailer-prompt/main/commit.py')

for line in scriptFile.text.splitlines():
  version_line = line.split(' = ')

  if "version =" in line and version_line[0] == 'version' and int(version_line[1]) < version:
    print(bcolors.HEADER)
    print('=====================================================================================')
    print(' A newer version of git-trailer-prompt is available.')
    print(f' Your current version is v{version}. Update to v{version_line[1]} now!')
    print(' Run the git-trailer-prompt script with the `--update` argument or follow the')
    print(' README.md on https://github.com/mbrammer/git-trailer-prompt for manual installation.')
    print('=====================================================================================')
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

  with console.status("[bold green]Working on commit...") as status:
    os.system(f"git commit -m '{answers_changelog['message']}' --trailer 'Changelog: {trailer[0]}'")
    # repo.git.commit('-m', answers_changelog["message"], trailer=f'Changelog: {trailer[0]}')
else:
  questions_commit = [
    inquirer.Text('message', message='Please provide a commit message'),
  ]

  answers_commit = inquirer.prompt(questions_commit)

  with console.status("[bold green]Working on commit...") as status:
    os.system(f"git commit -m '{answers_commit['message']}'")
    # repo.git.commit('-m', answers_commit["message"])
