#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 15:13:07 2026

@author: and
"""

import json
from flask import Flask, jsonify, request
import asyncio


async def run():
    
   
    

    app = Flask(__name__)
    

    
    @app.route('/set_temperature', methods=['POST'])
    async def send_message():
     
        data_dict = json.loads(request.data)
        if 'message' in data_dict.keys():
            
            with open('data/display_message.txt','w+') as fid:
                
                fid.writelines(data_dict['message'])
           
           
            
            
        # elif:
            
    
        return jsonify('Message sent'), 200
    

    app.run(host="0.0.0.0", port=5000)
    
    
if __name__ == '__main__':
   
   
    asyncio.run(run())
    