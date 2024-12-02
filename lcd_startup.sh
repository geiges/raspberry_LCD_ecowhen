#!/bin/bash
eval $(ssh-agent)

git pull
echo "Starting python"

timedatectl # get time 
#tmux new-session -d -s lcd "python lcd_test_renewable.py"
python raspberry_liquid_16x2LDC_renewable_share.py

exit 0
