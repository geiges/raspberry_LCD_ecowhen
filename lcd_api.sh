#!/bin/bash
eval $(ssh-agent)
while  :

do
    git pull
    
    echo "Starting LDC API service"

    uv run rest_api_display.py

   sleep 30
done
exit 0
