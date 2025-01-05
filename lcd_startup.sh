#!/bin/bash
eval $(ssh-agent)
while  :

do
    git pull
    echo "Starting LDC display service"

    timedatectl # get time 
    #tmux new-session -d -s lcd "python lcd_test_renewable.py"
    python main.py
    sleep 10
done
exit 0
