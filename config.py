#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'auto-filter-bot-v3')
API_ID = int(environ['29441782'])
API_HASH = environ['fcd2518e068b5a42cd8fa40bdb76302a']
BOT_TOKEN = environ['6255291464:AAHmf1Ed9X7uv4ebUV_I4s_bIyAVVJ7Wc2I']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", "-1001754886821"))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "6019216032").split())
DB_URL = os.environ.get("DATABASE_URI", "mongodb+srv://thoppimoviebot:thoppimoviebot@thoppimoviebot.a3lj0ir.mongodb.net/?retryWrites=true&w=majority")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
DEV_CHANNEL = "https://t.me/rithikclicks"

# MongoDB information
DATABASE_URI = environ['mongodb+srv://thoppimoviebot:thoppimoviebot@thoppimoviebot.a3lj0ir.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['thoppimoviebot']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm [THOPPI THE MOVIE BOT]**

Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>Join [MALLU OTT RELEASE](https://t.me/mallu_ott_release) FOR NEW MOVIES</b>\n\n<code>{file_name}</code>\nSize{file_size}\n{file_caption}.")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
