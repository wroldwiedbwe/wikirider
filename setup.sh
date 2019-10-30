#!/bin/bash

echo -e "\e[1;32mInstalling wikirider...\e[0m"

CUR_DIR=$(pwd)

# if an arg is passed, use this as install location
if  [ "$1" ] ; then
    INSTALL_LOC=$1
    rsync -a --exclude=.* $CUR_DIR $INSTALL_LOC
else
    set INSTALL_LOC=$CUR_DIR
fi

FULL_LOC=$INSTALL_LOC/wikirider
cd $FULL_LOC

echo -e "\e[1;32mInstall location is $FULL_LOC"

if $(hash pip 2>/dev/null); then
    PIP="pip"
elif $(hash pip3 2>/dev/null); then
    PIP="pip3"
else
    echo -e "\e[1;31mpip is not currently installed, please install it\e[0m"
    exit 1
fi

if $PIP install virtualenv && virtualenv .env && source $(pwd)/.env/bin/activate && $PIP install -r requirements.txt; then
    echo -e "\e[1;32mInstallation complete!"
    echo -e "To run wikirider, do \e[0;33m'cd $FULL_LOC; source .env/bin/activate && python wikirun.py'\e[1;32m!"
    echo -e "Don't forget to do \e[0;33m'deactivate'\e[1;32m after you're done to exit the virtualenv!\e[0m"
else
    echo -e "\e[1;31mSome errors occured! Look up to see what went wrong.\e[0m"
fi
cd $CUR_DIR
