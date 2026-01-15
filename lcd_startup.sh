#!/bin/bash
eval $(ssh-agent)
while  :

do
    git pull
    
    if (( $(curl http://localhost:5000/alive) != yes)); then
        echo "Starting Rest api"
        tmux new-session -d -s restapi "uv run rest_api_display.py"
    fi
    echo "Starting LDC display service"

    timedatectl # get time 
    #tmux new-session -d -s lcd "python lcd_test_renewable.py"
    python main.py
    sleep 10
done
exit 0
