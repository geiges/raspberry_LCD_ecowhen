#!/bin/bash
cd /home/and/python/clean_energy_forcast/shared
git pull
timedatectl # get time 
#tmux new-session -d -s lcd "python lcd_test_renewable.py"
python raspberry_liquid_16x2LDC_renewable_share.py

exit 0
