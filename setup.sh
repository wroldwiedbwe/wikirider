#!/bin/bash

echo -e "\e[1;32mInstalling wikirider...\e[0m"

command -v pip >/dev/null 2>&1 || { echo >&2 "I require pip but it's not installed.  Aborting."; exit 1; }
PYVER=$(python -V 2>&1 | grep -Po '(?<=Python )(\d)')
CUR_DIR=$(pwd)
PY="python"

if [[ `command -v python3` ]]; then
    export PYVER="3";
    export PY="python3";
fi

if [[ $PYVER -ne "3" ]]; then
    echo -e "\e[1;31mOnly Python 3.x is supported! Make sure $(command -v python) links to Python 3.x\e[0m";
    exit;
fi

# if an arg is passed, use this as install location
if  [ "$1" ] ; then
    INSTALL_LOC=$1
    rsync -a --exclude=.* $CUR_DIR $INSTALL_LOC
else
    export INSTALL_LOC=$CUR_DIR
fi

export FULL_LOC="$INSTALL_LOC/wikirider"
export OLD_LOC="$CUR_DIR"
rm -rf "$FULL_LOC"
mkdir -p "$FULL_LOC"
cd "$FULL_LOC"

echo -e "\e[1;32mInstall location is $FULL_LOC"

if $(hash pip 2>/dev/null); then
    PIP="pip"
elif $(hash pip3 2>/dev/null); then
    PIP="pip3"
else
    echo -e "\e[1;31mpip is not currently installed, please install it\e[0m"
    exit 1
fi

export CUR_DIR=$(pwd)

if $PIP install virtualenv && virtualenv .env -p $PY && source "$CUR_DIR/.env/bin/activate" && $PIP install -r "$OLD_LOC/requirements.txt"; then
    echo -e "\e[1;32mInstallation complete!"
    echo -e "To run wikirider, do \e[0;33m'cd $FULL_LOC; source .env/bin/activate && python wikirun.py'\e[1;32m!"
    echo -e "Don't forget to do \e[0;33m'deactivate'\e[1;32m after you're done to exit the virtualenv!\e[0m"
else
    echo -e "\e[1;31mSome errors occured! Look up to see what went wrong.\e[0m"
fi
cd "$CUR_DIR"
