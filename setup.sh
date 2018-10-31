#!/bin/bash

# This is a program for installing the whole project. 

# 20181029 version alpha 1
# The code work

if [ "$#" -ne 1 ]; then
    echo "Error!\nThe number of parameters is wrong"
    echo "Usage:    ${0##*/} [options]"
    echo "Available options: install, uninstall, clean"
    exit 1
fi

option=${1}

if [ "${option}" = 'install' ]; then
    ln -s $PWD/'update_to_TAT_db.py' '/usr/local/bin/update_to_TAT_db.py'
    exit 0
fi

if [ "${option}" = 'uninstall' ]; then
    rm '/usr/local/bin/update_to_TAT_db.py'
    exit 0
fi

if [ "${option}" = 'clean' ]; then
    rm $PWD/log.txt
    exit 0
fi

echo "No matched options"
echo "Available options: install, uninstall, clean"
exit 1
