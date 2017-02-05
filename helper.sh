 #!/usr/bin/env bash

set -e # Exit on errors


# Helper script to prepare the computers for the Python course
# 
# git is already installed
# 
# we install pyenv, pyenv-build and pyenv-virtualenv
#
# We update the .bashrc (cuz mate-terminal does not look at .profile nor .bash_profile
# 
# We install 3.5.0
#
# We upgrade pip
# 
# We install jupyter


git clone https://github.com/yyuu/pyenv.git ~/.pyenv
pushd ~/.pyenv
git pull
popd

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils

git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

cat >> .bashrc <<'EOF'
export PATH

export PYENV_ROOT="$HOME/.pyenv"
[[ "$PATH" =~ "$PYENV_ROOT/bin" ]] || PATH="$PYENV_ROOT/bin:$PATH"


if which pyenv > /dev/null; then
    eval "$(pyenv init -)";
    eval "$(pyenv virtualenv-init -)"
fi
EOF


pyenv install 3.5.0

pip install --upgrade pip

pip install jupyter
