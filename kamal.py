# -*- coding: utf-8 -*-

from colorama import init, Fore, Style
from pyrogram import Client, filters, errors, raw
from telethon.sync import TelegramClient
from termcolor import colored
import os, csv, random, time, base64, re, sys, requests, logging
from pyrogram.errors import UserPrivacyRestricted, PeerFlood, PeerIdInvalid, SessionRevoked, UserNotParticipant, UserNotMutualContact, UserAlreadyParticipant, UserChannelsTooMuch, UserIdInvalid, UserKicked, ChatAdminRequired, UserBannedInChannel, RPCError, PhoneNumberUnoccupied, PhoneNumberInvalid, PhoneNumberOccupied, PhoneNumberBanned, PhoneNumberFlood, UsernameNotOccupied, UserDeactivated, UserDeactivatedBan, AuthKeyUnregistered, PhonePasswordFlood
from pyrogram.errors import BadRequest, UsernameInvalid, ChannelsTooMuch
from pyrogram.raw.functions.auth import ResetAuthorizations
from pyrogram.raw.functions.account import GetAuthorizations, ResetAuthorization
from pyrogram.errors import FloodWait
from pyrogram import utils
from pyrogram.raw import functions, types
from pyrogram.enums import UserStatus
from pyrogram.enums import ParseMode
from pyrogram.errors import BadRequest
from pyrogram import idle
import platform
import geocoder
from subprocess import call
import configparser
import webbrowser
from time import sleep
from threading import Thread, active_count
from emailtools import generate
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import phonenumbers
from phonenumbers import PhoneNumberFormat
from bs4 import BeautifulSoup
from faker import Faker
from datetime import datetime, timedelta
from os import system, name
from re import search, compile
import string
import asyncio

fake = Faker()
n = Fore.RESET
def banner():
    b = [
        ('██╗░░██╗░█████╗░███╗░░░███╗░█████╗░██╗░░░░░ ((/2\\•/4\\))', 0.1),
        ('██║░██╔╝██╔══██╗████╗░████║██╔══██╗██║░░░░░ (/_)(\\/)(_))', 0.1),
        ('█████═╝░███████║██╔████╔██║███████║██║░░░░░ (()((_)((_)\)', 0.1),
        ('██╔═██╗░██╔══██║██║╚██╔╝██║██╔══██║██║░░░░░  | __| /  (_)', 0.1),
        ('██║░╚██╗██║░░██║██║░╚═╝░██║██║░░██║███████╗  |__ \\| () |', 0.1),
        ('╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝  |___(_)__/', 0.2)
    ]
    for line, sleep_time in b:
        print(colored(f'{line}{n}', 'green', attrs=['bold']))
        time.sleep(sleep_time)
    print(colored(f' Coded By: @kamal939 & @bd71zone_team | Version: 5.2.4.9 ', 'yellow', 'on_blue', attrs=['bold']) + n)

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def animate_texts(texts, delay=0.00005):
    for text in texts:
        animate_text(text, delay)

def animate_text(text, delay=0.005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def is_android():
        if os.path.exists('/system/app') or os.path.exists('/system/priv-app') or os.environ.get('ANDROID_ROOT') or os.environ.get('ANDROID_DATA'):
            return True
        return False

active_file_path = ""

folder_path = ''
if is_android():
    base_dir = '/storage/emulated/0/Android/media/org.facebook.katana/'
    folder_path = '/storage/emulated/0/Android/media/org.facebook.katana/tmp/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/facebook/file/facebook file/folder/metrics/opaux2/conf/lib/tmp/storage/data/volume/'
    session_path = os.path.join(base_dir, 'kerneI/depth1/net/disk/metrics/opaux2/conf/lib/tmp/logs/proc/info/metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/')
    
    u_path = os.path.join(base_dir, 'user/depth1/depth2/metrics/opaux2/conf/lib/tmp/logs/proc/depth3/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    op_path = os.path.join(base_dir, 'Facebook/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    path_1 = os.path.join(base_dir, 'tmp/module2/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_2 = os.path.join(base_dir, 'tmp/module/depth2/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_3 = os.path.join(base_dir, 'tmp/module/depth1/depth3/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/')
    path_4 = os.path.join(base_dir, 'tmp/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/')
    path_5 = os.path.join(base_dir, 'tmp/module/depth1/depth2/depth3/net/metrics/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/')
    path_6 = os.path.join(base_dir, 'tmp/module/depth1/depth2/depth3/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/')
    
    path_7 = os.path.join(base_dir, 'Facebook/depth2/depth3/metrics/opaux2/conf/lib/depth34/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_8 = os.path.join(base_dir, 'Facebook/depth0/depth1/metrics/opaux2/conf/lib/depth38/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_9 = os.path.join(base_dir, 'Facebook/depth1/depth3/metrics1/opaux27/conf/lib/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_10 = os.path.join(base_dir, 'Facebook/depth1/depth2/metrics/opaux24/conf/lib/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    path_11 = os.path.join(base_dir, 'user/depth1/depth24/metrics/opaux2/conf/lib/tmp/logs/proc8/depth3/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_12 = os.path.join(base_dir, 'user/depth1/depth2/metrics/opaux2/conf5/lib/tmp7/logs/proc/depth3/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_13 = os.path.join(base_dir, 'user/depth1/depth2/metrics/opaux2/conf/lib/tmp/log/proc/depth3/net/disk/info/metrics/opaux2/conf/')
    
    path_14 = os.path.join(base_dir, 'config/depth1/depth2/proc/net5/disk/metrics/opaux2/conf/lib/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_15 = os.path.join(base_dir, 'config/depth2/depth2/proc/net/disk/metrics2/opaux2/conf/lib/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_16 = os.path.join(base_dir, 'config/depth1/depth2/proc/net/disk/metrics/opaux24/conf/lib/net/disk/metrics/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    path_17 = os.path.join(base_dir, 'module/depth2/depth2/depth3/net/metrics/opaux2/conf/disk/info/opaux2/conf/lib/depth3/depth4/kernel/depth1')
    path_18 = os.path.join(base_dir, 'module/depth1/depth2/depth2/net/metrics/opaux2/conf/disk/info/opaux2/conf/lib/depth3/depth4/kernel/depth1')
    path_19 = os.path.join(base_dir, 'module/depth1/depth2/depth3/net/metrics/opaux1/conf/disk/info/opaux2/conf/lib/depth3/depth4/kernel/depth1')
    
    path_20 = os.path.join(base_dir, 'kerneI/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/kernel/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4//metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/')
    path_21 = os.path.join(base_dir, 'kerneI/depth2/depth2/metrics/opaux2/conf/lib/depth3/depth4/kernel/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/')
    path_22 = os.path.join(base_dir, 'kerneI/depth3/depth2/metrics/opaux2/conf/lib/depth3/depth4/kernel/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/')
    path_23 = os.path.join(base_dir, 'kerneI/depth1/depth2/metrics/opaux24/conf/lib/depth3/depth4/kernel/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/')
    path_24 = os.path.join(base_dir, 'kerneI/depth1/depth2/metrics/opaux2/conf/lib1/depth3/depth4/kernel/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/')
    path_25 = os.path.join(base_dir, 'kerneI/depth1/depth2/metrics2/opaux2/conf/lib/depth3/depth4/kernel/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/metrics/opaux2/conf/disk/info/logs/proc/net/disk/info/meta/vol1/depth/infonet/')
    
    x_path = os.path.join(base_dir, 'xbox/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    f_path = os.path.join(base_dir, 'flog/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    me_path = os.path.join(base_dir, 'manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    
elif os.name == 'nt':
    base_dir = 'c:/system file/'
    folder_path = 'c:/system file/operator/opaux/conf/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/module/depth1/depth2/depth3/nets/metrics/opaux2/conf/disk/info/logs/proc/net/disk/'
    m_path = os.path.join(base_dir, 'module/depth1/depth2/depth3/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    y_path = os.path.join(base_dir, 'support/depth1/depth2/info/meta/vol1/depth/metrics/opaux2/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    session_path = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/metrics/opaux2/conf/lib/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/logs/proc/')
    u_path = os.path.join(base_dir, 'user/depth1/depth2/depth3/metrics/opaux2/conf/lib/tmp/logs/proc/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    op_path = os.path.join(base_dir, 'network/depth1/depth2/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    path_1 = os.path.join(base_dir, 'operator/opaux/cong/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/logs/proc/net/disk/')
    path_2 = os.path.join(base_dir, 'module/depth2/depth2/depth3/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_3 = os.path.join(base_dir, 'support/depth2/depth2/info/meta/vol1/depth/metrics/opaux2/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_4 = os.path.join(base_dir, 'wards/depth2/metrics/opaux2/metrics/opaux2/conf/lib/metrics/opaux2/conf/lib/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/')
    path_5 = os.path.join(base_dir, 'user/depth2/depth2/depth3/metrics/opaux2/conf/lib/tmp/logs/proc/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_6 = os.path.join(base_dir, 'network/depth2/depth2/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    path_7 = os.path.join(base_dir, 'operator/opaux/conf/lib/tmp/logs/pro/net/disk/info/meta/vol1/depth/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/logs/proc/net/disk/')
    path_8 = os.path.join(base_dir, 'module/depth3/depth2/depth3/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_9 = os.path.join(base_dir, 'support/depth1/depth2/info/meta/vol1/depth/metrics/opaux2/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_10 = os.path.join(base_dir, 'wards/depth1/metrics1/opaux2/metrics/opaux2/conf/lib/metrics/opaux2/conf/lib/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/')
    path_11 = os.path.join(base_dir, 'user/depth1/depth3/depth3/metrics/opaux2/conf/lib/tmp/logs/proc/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_12 = os.path.join(base_dir, 'network/depth1/depth4/depth3/depth4/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    path_13 = os.path.join(base_dir, 'operator/opaux2/conf/lib/tmp/logs/pro/net4/disk/info/meta/vol1/depth/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/logs/proc/net/disk/')
    path_14 = os.path.join(base_dir, 'module/depth1/depth1/depth3/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_15 = os.path.join(base_dir, 'support/depth1/depth2/info2/meta/vol1/depth/metrics/opaux2/meta/vol1/depth/metrics/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_16 = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/metrics1/opaux2/conf/lib/meta/vol1/depth/metrics/metrics/opaux2/conf/lib/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/')
    path_17 = os.path.join(base_dir, 'user/depth1/depth2/depth3/metrics/opaux22/conf/lib/tmp/logs/proc/meta/vol1/depth/metrics/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_18 = os.path.join(base_dir, 'network/depth1/depth2/depth1/depth4/meta/vol1/depth/metrics/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    path_19 = os.path.join(base_dir, 'operator/opaux/conf/lib/tmp/logs/proc/net/disk/info/meta/vol/depth/storage/data/volume/module/depth1/depth2/depth3/net2/metrics/opaux2/conf/disk/info/logs/proc/net/disk/')
    path_20 = os.path.join(base_dir, 'operator/opaux2/conf/lib/tmp/logs/proc/net/disk/info/meta/vol2/depth/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/logs/proc/net/disk/')
    path_21 = os.path.join(base_dir, 'module/depth1/depth2/depth4/net/disk/info/depth2/depth4/net/disk/info/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_22 = os.path.join(base_dir, 'support/depth1/depth3/info/meta/vol1/depth/metrics/opaux2/meta/vol1/depth/metrics/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_23 = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/metrics/opaux2/conf2/lib/meta/vol1/depth/metrics/opaux2/conf/lib/storage/data/volume/module/depth1/depth2/depth3/net/metrics/opaux2/conf/')
    path_24 = os.path.join(base_dir, 'user/depth1/depth2/depth4/metrics1/opaux2/conf/lib/tmp/logs/proc/meta/vol1/depth/metrics/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    path_25 = os.path.join(base_dir, 'network/depth1/depth7/depth4/depth4/meta/vol1/depth/metrics/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/')
    
    x_path = os.path.join(base_dir, 'xbox/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    f_path = os.path.join(base_dir, 'data/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    me_path = os.path.join(base_dir, 'manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    
elif os.name == 'posix':
    if platform.system() == 'Darwin':  # MacOS
        base_dir = '/Users/system file/'
        folder_path = '/Users/system file/vnom/net/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk/infos/meta/vol1/depth/storage/data/volume/'
        m_path = os.path.join(base_dir, 'module/depth1/depth2/depth3/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        y_path = os.path.join(base_dir, 'config/depth1/depth2/info/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        session_path = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/proc/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        u_path = os.path.join(base_dir, 'user/depth1/depth2/depth3/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        op_path = os.path.join(base_dir, 'network/depth1/depth2/depth3/depth4/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_1 = os.path.join(base_dir, 'vnom/net/disk2/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        path_2 = os.path.join(base_dir, 'module/depth2/depth2/depth3/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_3 = os.path.join(base_dir, 'config/depth2/depth2/info/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_4 = os.path.join(base_dir, 'wards/depth2/metrics/opaux2/proc/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_5 = os.path.join(base_dir, 'user/depth2/depth2/depth3/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_6 = os.path.join(base_dir, 'network/depth1/depth2/depth3/depth4/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_7 = os.path.join(base_dir, 'vnom/net/disk/info/meta/vol2/depth/storage/data/volume2/opaux2/conf/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        path_8 = os.path.join(base_dir, 'module/depth1/depth3/depth3/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_9 = os.path.join(base_dir, 'config/depth1/depth3/info/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_10 = os.path.join(base_dir, 'wards/depth1/metric/opaux2/proc/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_11 = os.path.join(base_dir, 'user/depth1/depth3/depth3/meta/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_12 = os.path.join(base_dir, 'network/depth1/depth3/depth3/depth4/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_13 = os.path.join(base_dir, 'vnom/net/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk1/info/meta/vol1/depth/storage/data/volume/')
        path_14 = os.path.join(base_dir, 'module/depth1/depth2/depth3/net2/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_15 = os.path.join(base_dir, 'config/depth1/depth2/info/meta2/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_16 = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/proc2/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_17 = os.path.join(base_dir, 'user/depth1/depth2/depth3/meta2/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_18 = os.path.join(base_dir, 'network/depth1/depth2/depth3/depth1/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_19 = os.path.join(base_dir, 'vnom/vet/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        path_20 = os.path.join(base_dir, 'vnom/net/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lim/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        
        path_21 = os.path.join(base_dir, 'module/depth1/depth2/depth1/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_22 = os.path.join(base_dir, 'config/depth1/depth2/info1/meta/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_23 = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/procs/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_24 = os.path.join(base_dir, 'user/depth1/depth2/depth1/meta/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_25 = os.path.join(base_dir, 'network/depth1/depth2/depth1/depth4/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        x_path = os.path.join(base_dir, 'xbox/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
        f_path = os.path.join(base_dir, 'data/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
        me_path = os.path.join(base_dir, 'manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    
    else:
        base_dir = '/home/system file/'
        folder_path = '/home/system file/vnom/net/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk/infos/meta/vol1/depth/storage/data/volume/'
        m_path = os.path.join(base_dir, 'module/depth1/depth2/depth3/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        y_path = os.path.join(base_dir, 'config/depth1/depth2/info/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        session_path = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/proc/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        u_path = os.path.join(base_dir, 'user/depth1/depth2/depth3/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        op_path = os.path.join(base_dir, 'operation1/depth1/depth2/depth3/depth4/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_1 = os.path.join(base_dir, 'vnom/net/disk2/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        path_2 = os.path.join(base_dir, 'module/depth2/depth2/depth3/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_3 = os.path.join(base_dir, 'config/depth2/depth2/info/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_4 = os.path.join(base_dir, 'wards/depth2/metrics/opaux2/proc/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_5 = os.path.join(base_dir, 'user/depth2/depth2/depth3/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_6 = os.path.join(base_dir, 'operation2/depth1/depth2/depth3/depth4/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_7 = os.path.join(base_dir, 'vnom/net/disk/info/meta/vol2/depth/storage/data/volume2/opaux2/conf/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        path_8 = os.path.join(base_dir, 'module/depth1/depth3/depth3/net/disk/info/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_9 = os.path.join(base_dir, 'config/depth1/depth3/info/meta/vol1/depth/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_10 = os.path.join(base_dir, 'wards/depth1/metric/opaux2/proc/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_11 = os.path.join(base_dir, 'user/depth1/depth3/depth3/meta/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_12 = os.path.join(base_dir, 'operation1/depth1/depth3/depth3/depth4/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_13 = os.path.join(base_dir, 'vnom/net/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk1/info/meta/vol1/depth/storage/data/volume/')
        path_14 = os.path.join(base_dir, 'module/depth1/depth2/depth3/net2/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_15 = os.path.join(base_dir, 'config/depth1/depth2/info/meta2/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_16 = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/proc2/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_17 = os.path.join(base_dir, 'user/depth1/depth2/depth3/meta2/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_18 = os.path.join(base_dir, 'operation1/depth1/depth2/depth3/depth1/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        path_19 = os.path.join(base_dir, 'vnom/vet/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lib/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        path_20 = os.path.join(base_dir, 'vnom/net/disk/info/meta/vol1/depth/storage/data/volume/opaux2/conf/lim/tmp/logs/proc/net/disk/info/meta/vol1/depth/storage/data/volume/')
        
        path_21 = os.path.join(base_dir, 'module/depth1/depth2/depth1/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_22 = os.path.join(base_dir, 'config/depth1/depth2/info1/meta/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_23 = os.path.join(base_dir, 'wards/depth1/metrics/opaux2/procs/net/disk/info/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_24 = os.path.join(base_dir, 'user/depth1/depth2/depth1/meta/vol1/depth/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        path_25 = os.path.join(base_dir, 'operation1/depth1/depth2/depth1/depth4/opaux2/conf/lib/tmp/logs/proc/net/disk/manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/')
        
        x_path = os.path.join(base_dir, 'xbox/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
        f_path = os.path.join(base_dir, 'data/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
        me_path = os.path.join(base_dir, 'manager/depth1/depth2/metrics/opaux2/conf/lib/depth3/depth4/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/module/depth1/depth2/depth3/net/metrics/opaux2/conf/disk/info/')
    
else:
    folder_path = './'

active_file_path = os.path.join(folder_path, "infomata.txt")

os.makedirs(folder_path, exist_ok=True)
os.makedirs(m_path, exist_ok=True)
os.makedirs(y_path, exist_ok=True)
os.makedirs(session_path, exist_ok=True)
os.makedirs(u_path, exist_ok=True)
os.makedirs(op_path, exist_ok=True)
os.makedirs(path_1, exist_ok=True)
os.makedirs(path_2, exist_ok=True)
os.makedirs(path_3, exist_ok=True)
os.makedirs(path_4, exist_ok=True)
os.makedirs(path_5, exist_ok=True)
os.makedirs(path_6, exist_ok=True)
os.makedirs(path_7, exist_ok=True)
os.makedirs(path_8, exist_ok=True)
os.makedirs(path_9, exist_ok=True)
os.makedirs(path_10, exist_ok=True)
os.makedirs(path_11, exist_ok=True)
os.makedirs(path_12, exist_ok=True)
os.makedirs(path_13, exist_ok=True)
os.makedirs(path_14, exist_ok=True)
os.makedirs(path_15, exist_ok=True)
os.makedirs(path_16, exist_ok=True)
os.makedirs(path_17, exist_ok=True)
os.makedirs(path_18, exist_ok=True)
os.makedirs(path_19, exist_ok=True)
os.makedirs(path_20, exist_ok=True)
os.makedirs(path_21, exist_ok=True)
os.makedirs(path_22, exist_ok=True)
os.makedirs(path_23, exist_ok=True)
os.makedirs(path_24, exist_ok=True)
os.makedirs(path_25, exist_ok=True)
os.makedirs(x_path, exist_ok=True)
os.makedirs(f_path, exist_ok=True)
os.makedirs(me_path, exist_ok=True)

try:
    open(active_file_path, "a").close()
except PermissionError as e:
    print(colored("Your Device Does Not Support This Script", "red", attrs=["bold"]))
    sys.exit()
except OSError as error:
    print(colored("Your Device Does Not Support This Script", "red", attrs=["bold"]))
    exit()

with open(active_file_path, "r") as f:
    activation_status = f.read().strip()
if "6g456d5f4g6y789dfg768fds79gydf74hg68dffh4gby98st146y7419yhb187ty1bht7" in activation_status.lower():
    print(colored("\n😎 Hey Dear This Is Just For Test 😎😃\n😎 You Have To Pay To Get Original Code 😎😃", "red", attrs=["bold"]))
else:
    clr()
    banner()
    texts = [
        colored("\nYou Not Activated Please Activate Your Script", "red", attrs=["bold"])
    ]
    animate_texts(texts)
    api_id = "20058531"
    api_hash = "2d2081decbd52c42f99151b4c7bb8743"
    bot_token = "6679512772:AAGlrZYTsscyvLkMcCPiPgdhI1nHjtTDKBY"

    activation_code = random.randint(105424554575459632100, 99457913648756279861354)
    deactivation_code = random.randint(10542455454875457896, 99457913648756215798)
    
    
    current_time = datetime.now()
    device = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    ip = geocoder.ip('me').ip
    time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    reason = 'Request For Activation'

    def format_message(message):
        parts = message.split(": ")
        if len(parts) > 1 and "code" in parts[0].lower():
            formatted_message = f"**{parts[0]}**: `{parts[1]}`"
        else:
            formatted_message = f"**{parts[0]}**: {parts[1]}" if len(parts) > 1 else f"**{message}**"
        return formatted_message

    message_kamal_send = "\n".join([
        format_message(f"From kamal Test"),
        format_message(f"Reason: {reason}"),
        format_message(f"Activation Code: {activation_code}"),
        format_message(f"Date And time: {time}"),
        format_message(f"UserDevice: {device}"),
        format_message(f"Node: {node}"),
        format_message(f"Release: {release}"),
        format_message(f"Version: {version}"),
        format_message(f"Machine: {machine}"),
        format_message(f"Processor: {processor}"),
        format_message(f"Ip Location: {ip}"),
        format_message(f"Deactivation code: {deactivation_code}")
    ])

    stop_event = asyncio.Event()
    
        
    async def main():
        async with Client(os.path.join(session_path, 'data2'), api_id=api_id, api_hash=api_hash, bot_token=bot_token) as app:
            await app.send_message("@kamal939", message_kamal_send, parse_mode=ParseMode.MARKDOWN)
            
            print(colored("Your Activation Code: ", "green", attrs=["bold"]) + colored(f"{activation_code}", "yellow", attrs=["bold"]))
            print(colored("\nYou Need To Activate To Access This Script\nSend Your Activation Code To @kamal939", "cyan", attrs=["bold"]))
            print(colored("\nWaiting For The Script To Be Activated", "blue", attrs=["bold"]))
            
            @app.on_message(filters.chat("@kamal939"))
            async def handle_message(client, message):
                try:
                    received_code = int(message.text.strip())
                    
                    if received_code == activation_code:
                        activation_message = "\n".join([
                            format_message(f"From Kamal Test"),
                            format_message(f"Activation code: {activation_code}"),
                            format_message(f"Deactivation Code: {deactivation_code}"),
                            format_message(f"Status: Activated")
                        ])
                        await app.send_message("@kamal939", activation_message, parse_mode=ParseMode.MARKDOWN)
                        print(colored("\nCongratulation! Your Script Successfully Activated", "green", attrs=["bold"]))
                        with open(active_file_path, "w") as f:
                            f.write("6g456d5f4g6y789dfg768fds79gydf74hg68dffh4gby98st146y7419yhb187ty1bht7")
                        stop_event.set()
                        return
                    
                    elif received_code == deactivation_code:
                        deactivation_message = "\n".join([
                            format_message(f"From Kamal Test"),
                            format_message(f"Activation code: {activation_code}"),
                            format_message(f"Deactivation Code: {deactivation_code}"),
                            format_message(f"Status: Deactivated")
                        ])
                        await app.send_message("@kamal939", deactivation_message, parse_mode=ParseMode.MARKDOWN)
                        print(colored("\nYour Script Could Not Be Activated\nContact @kamal939 For Details", "red", attrs=["bold"]))
                        stop_event.set()
                        return
                except ValueError:
                    pass

            await stop_event.wait()

    if __name__ == "__main__":
        try:
            asyncio.run(main())
        except (KeyboardInterrupt, SystemExit):
            print("Script interrupted.")