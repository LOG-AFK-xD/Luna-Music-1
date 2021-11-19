import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Harsh_shukla_xd")
ALIVE_NAME = getenv("ALIVE_NAME", "Luna")
BOT_USERNAME = getenv("BOT_USERNAME", "Luna_MusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Luna_x_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "The_Secret_worlds")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Team_Blaze_Fighter")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/0b7b6460e1dc3a8bbf5be.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/unknownvip/Luna-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
