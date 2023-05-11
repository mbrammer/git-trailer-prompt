# Git trailer prompt

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
   - Add it to you PATH variable to call globally
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