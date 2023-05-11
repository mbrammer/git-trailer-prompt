#!python3

import inquirer
import git

repo = git.Repo('.')
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
