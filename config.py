#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 12:31:17 2026

@author: and
"""
import os 


temp_folder = "/dev/shm/raspberry_LCD_display"

os.makedirs(temp_folder,exist_ok=True)
temp_file_display_message1 = os.path.join(temp_folder,
                                           "display1.txt")