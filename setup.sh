#!/bin/bash

pip3 install -r requirements.txt
chmod +x commit.py

if [ -d "/usr/local/bin" ]; then
  echo ""
  echo "Installing script to /usr/local/bin... (you need to provide password!)"
  sudo mv ./commit.py /usr/local/bin/commit.py
  echo "DONE!"
  echo ""
  echo "Deleting installation directory..."
  cd ..
  rm -rf git-trailer-prompt
  echo "DONE!"
  echo ""
  echo "You should now be able to call the script with 'commit.py' globally from every directory."
else
  echo "Couldn't find /usr/local/bin on you machine."
  echo "If you want to use the script globally, you need to do this setup on your own. Otherwise you have to call the commit.py inside the directory where it's stored."
fi
