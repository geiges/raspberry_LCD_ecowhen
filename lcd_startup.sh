#!/bin/bash
eval $(ssh-agent)

git pull
echo "Starting python"

timedatectl # get time 
#tmux new-session -d -s lcd "python lcd_test_renewable.py"
python lcd_main.py

exit 0
