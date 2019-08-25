#!/bin/bash

echo -e "\e[1;32mInstalling wikirider...\e[0m"

if pip install virtualenv && virtualenv .env && source $(pwd)/.env/bin/activate && pip install -r requirements.txt;
then
    echo -e "\e[1;32mInstallation complete!"
    echo -e "To run wikirider, do \e[0;33m'source .env/bin/activate && python wikirun.py'\e[1;32m!"
    echo -e "Don't forget to do \e[0;33m'deactivate'\e[1;32m after you're done to exit the virtualenv!\e[0m"
else
    echo -e "\e[1;31mSome errors occured! Look up to see what went wrong.\e[0m"
fi
