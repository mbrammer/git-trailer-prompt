# Git trailer prompt

This script will provide an easy way to do git commits with changelog trailers.  
It will let you choose if you want to provide a changelog commit or a usual commit.  
So this would basically replace the step of `git commit [...]`.

**Usual commit example:**
```
$ commit
[?] Do you want to create a changelog message (y/N): N

[?] Please provide a commit message: initial commit
```

**Changelog example:**
```
$ commit
[?] Do you want to create a changelog message (y/N): y

[?] Please select a changelog type ans press enter: fixed: Bug fix
   added: New feature
 > fixed: Bug fix
   changed: Feature change
   deprecated: New deprecation
   removed: Feature removal
   security: Security fix
   performance: Performance improvement
   other: Other

[?] Please provide a non-technical changelog message: Fixed the most hated bug
```

## Requirements
- Python3

## Installation

Just run
```
git clone git@github.com:mbrammer/git-trailer-prompt.git && cd git-trailer-prompt && sh ./setup.sh
```

For unix systems, the setup script should do the rest for you.  

**If you are running on Windows**, you need to do some manual setup.  
Follow these steps:
1. Add the commit.py script somewhere you want to store it
2. Pick one of these options:
   - Call it there from your project folder `my-git-repo/$ ./path/to/commit.py`
   - Add it to you PATH variable to call it globally
   - Create an alias to call it globally (see "Setting up an alias" below)

## Usage

Inside your project directory (which obviously should be a Git repo) just run `commit.py`

### Setting up an alias (optional)

If you want to call the script with another command, just create an alias in your bash profile.  
Here are some examples:
```
alias commit='commit.py'
alias git_commit='commit.py'
alias trailer_commit='commit.py'

# For Windows:
alias commit='/path/to/commit.py'
```
