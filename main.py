#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:41:10 2023

@author: Andreas Geiges
"""
import os
import time
#import git
import config

# repo = git.Repo(config.MAIN_REPO_PATH)
# repo.pull
import Adafruit_CharLCD as LCD


# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

debug = 0

# period for ssh update for new data and code
ssh_update_period = 1

lcd = LCD.Adafruit_CharLCD(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)

data_url = "https://github.com/geiges/Renewable_share_forecast_Germany/raw/main/DEU_RE_forecast.json"
    
# from clean_power_forecast import config
# model_version = config.active_models['DEU']


def show_display_message1(sleep_time=5):
    if os.path.exists(config.temp_file_display_message1):
        
        text = open(config.temp_file_display_message1,'r').readlines()[0]
        
        assert len(text) < 6
        lcd.set_cursor(0, 0)
        lcd.message(text.ljust(5))
        time.sleep(sleep_time)
        
    else:
        show_clock()    


def show_clock(sleep_time=5):
    
    lcd.set_cursor(0, 0)
    lcd.message(now.strftime('%H:%M'))
    for i in range(sleep_time//2):
        lcd.set_cursor(2, 0)
        lcd.message(' ')
        time.sleep(1)
        lcd.set_cursor(2, 0)
        lcd.message(':')
        time.sleep(1)
    


# create bar chars
lcd.create_char(
    8,
    [
        0x0,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
    ],
)
lcd.create_char(
    7,
    [
        0x0,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
    ],
)
lcd.create_char(
    6,
    [
        0x0,
        0x0,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
    ],
)
lcd.create_char(
    5,
    [
        0x0,
        0x0,
        0x0,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
    ],
)
lcd.create_char(
    4,
    [
        0x0,
        0x0,
        0x0,
        0x0,
        0x1F,
        0x1F,
        0x1F,
        0x1F,
    ],
)
lcd.create_char(3, [0x0, 0x0, 0x0, 0x0, 0x0, 0x1F, 0x1F, 0x1F])
lcd.create_char(2, [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F, 0x1F])
lcd.create_char(1, [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F])
lcd.create_char(0, [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
lcd.clear()
char_map = {
    0: '\x00',
    1: '\x01',
    2: '\x02',
    3: '\x03',
    4: '\x04',
    5: '\x05',
    6: '\x06',
    7: '\x07',
}
lcd.message('Welcome!')
time.sleep(0.2)
lcd.set_cursor(0, 1)
lcd.message('Starting...')

if debug:
    lcd.clear()
    char_map = {
        0: '\x00',
        1: '\x01',
        2: '\x02',
        3: '\x03',
        4: '\x04',
        5: '\x05',
        6: '\x06',
        7: '\x07',
        15: '\x01',
        14: '\x02',
        13: '\x03',
        12: '\x04',
        11: '\x05',
        10: '\x06',
        9: '\x07',
        8: chr(255),
    }
    while 1:
        for i in range(32):
            lcd.message('Process alive!' + char_map[i % 8] + char_map[i % 8])
            lcd.set_cursor(0, 1)
            msg = ''
            for j in range(lcd_columns):
                msg += char_map[(i + j) % 16]
            lcd.message(msg)
            time.sleep(0.5)
            lcd.clear()

            # lcd.mess11age(' Process alive!')
            # time.sleep(.5)

else:
    import pandas as pd

    # ssh_update()
    old_now = pd.Timestamp('now', tz='CET').round('1h') - pd.Timedelta(hours=1)
    while 1:
        force_refresh = False
        now = pd.Timestamp('now', tz='CET')
        now_round = now.round('1h')

        # update to every full hour in period
        # if (now_round.hour % ssh_update_period == 0) and (now.minute == 0):
        #     # pull update
        #     ssh_update()

        #     # force LCD refresh after update
        #     force_refresh = True

        if (now_round > old_now) or force_refresh:
            # update lcd
            df = pd.read_json(data_url).set_index('time')
            df.index = pd.DatetimeIndex(df.index, tz='CET')
            df['RE_share'] = (df['wind'] + df['solar'] + df['hydropower'] + df['biomass']) / df['demand']

            lcd.clear()
            lcd.message(now.strftime('%H:%M'))
            lcd.set_cursor(0, 1)
            lcd.message(f'RE:{df.loc[now_round, "RE_share"]*100:2.0f}%')
            offset = 5
            for hour in range(1, 11):
                ftime = now_round + pd.Timedelta(hours=hour)
                re_share = df.loc[ftime, "RE_share"] * 100

                if re_share > 100:
                    lcd.set_cursor(hour + offset, 1)
                    lcd.message('S')
                    lcd.set_cursor(hour + offset, 0)
                    lcd.message(char_map[int((re_share - 100) / 80 * 8)])
                elif re_share > 50:
                    lcd.set_cursor(hour + offset, 1)
                    lcd.message(chr(255))
                    lcd.set_cursor(hour + offset, 0)
                    lcd.message(char_map[int((re_share - 50) / 50 * 8)])
                else:
                    lcd.set_cursor(hour + offset, 1)
                    lcd.message(char_map[int((re_share) / 50 * 8)])
                    lcd.set_cursor(hour + offset, 0)
                    lcd.message(char_map[0])

            old_now = now_round
        else:
            print('Patiently waiting..')
            

        # time.sleep(60)

        for i in range(3):
           
            show_clock(sleep_time=6)
            show_display_message1(sleep_time=4)